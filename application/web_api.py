from src.user import User
from db.dbconnect import ClientDB
from flask import Flask, session, request, json, jsonify,app
from flask_session import Session
import json
import os

app = Flask(__name__)
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=os.urandom(16))
app.config.from_object(__name__)

def user_client_db(email,password):
    client = ClientDB(email=email,password=password)

    try:
        dados = client.email_get_pass()[0]
        if (password == dados[0]):
            return dados[1]
        else:
            return None
    except:
        return False
    

def companhia_to_aeropostos(companhia):
    cidades = []
    aero = []
    results = []
    client = ClientDB()

    try:
        db_results = client.getall_voo_to_companhia(companhia)
        for (_,_,src,dst,_,_,_,_) in db_results:
            cidades.append(src)
            cidades.append(dst)
        
        for city in cidades:
            db_pesquisa = client.getall_areo_to_cidade(city)
            for (_,nome,_,_,_) in db_pesquisa:
                aero.append(nome)
    
        for i,a in enumerate(aero):
            json_text = {'number': i, 'aeroposto': a}
            results.append(json_text)
    except:
        return None
    
    return results

def origem_to_aeropostos(origem):
    results = []
    client = ClientDB()

    try:
        db_results = client.getall_areo_to_cidade(origem)
        for i, (_,nome,_,_,_) in enumerate(db_results):
            json_text = {'number': i, 'aeroposto': nome}
            results.append(json_text)
    except:
        return None

    return results


def voo_to_data(dia,mes,ano):
    results = []
    client = ClientDB()
    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        db_results = client.get_voo_to_day(dia,mes,ano)
    
        for i, (id_voo,companhia) in enumerate(db_results):
            json_text = {'number': i+1, 'voo': id_voo, 'companhia': companhia}
            results.append(json_text)

        return results
    except:
        return None


def voo_to_tax_limit(number):
    results = []
    client = ClientDB()

    try:
        number = int(number)
        db_results = client.get_voo_to_minus_tarifas(number)
        
        for (id_voo,src,dst,comp) in db_results:
            json_text = {'voo': id_voo, 'origem': src,
                         'destino': dst, 'companhia': comp}
            results.append(json_text)
        return results
    except:
        return None

def db_compra(id_voo):
    results = []
    client = ClientDB()
    db_results = client.get_preco_to_id_voo(id_voo)
    if db_results is None:
        return {'status': False, 'messagem': 'not_disponivel'}
    precos = db_results[0]
    vagas = db_results[1]
    disponiveis = db_results[2]

    if disponiveis < 1:
        return {'status': False, 'messagem': 'not_disponivel'}
    else:
        client.update_voo_one(id_voo,disponiveis-1)
        return {'status': True, 'ticket': vagas, 'preco': precos, 'acento': disponiveis+1, 'sobrando': disponiveis}

    
            
@app.route('/')
def api_root():
    session.modified = True
    user = session.get('username')
    if user is not None:
        stringjs = {
            'status': True,
            'user' :  session.username}
        
        return jsonify(stringjs)

    return jsonify({'status': False, 'messagem': 'not_session'})


@app.route('/login', methods=['POST'])
def api_login():
    data = request.get_json() 
    email = data['email']
    password = data['password']

    db_login = user_client_db(email,password)
    print(db_login)
    if db_login is not None:
        session['username'] = db_login
        print(session)
        return jsonify({'status': True, 'messagem': 'conectado'})
  
    elif db_login is not None:
        return jsonify({'status': False, 'messagem': 'not_exist_user'})

    elif db_login is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})
 


@app.route('/logout') # Efetuar Logout
def api_logout():
    session.pop('username',None)
    return jsonify({'status': True, 'messagem': 'logout_sucess'})



@app.route('/areotocamp', methods=['POST']) # Retorna Aeroposto 
def areoposto_to_companhia():
    data = request.get_json() 
    companhia = data['companhia']
    
    json_text = companhia_to_aeropostos(companhia)
    if json_text is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})
    else:
        return jsonify(json_text)


@app.route('/areotoorigem', methods=['POST']) # Retorna Aeroposto to origem
def areoposto_to_origem():
    data = request.get_json() 
    origem = data['origem'].upper()
    json_text = origem_to_aeropostos(origem)
    if json_text is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})
    else:
        return jsonify(json_text)


@app.route('/vootoday', methods=['POST']) # Voo to data
def retornar_voo():
    data = request.get_json()
    dia = data['dia']
    mes = data['mes']
    ano = data['ano']
    json_text = voo_to_data(dia,mes,ano)
    
    if json_text is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})       
    else:
        return jsonify(json_text)


@app.route('/vootonumber', methods=['POST']) # Pesquisa Voo
def pesquisa_voo():
    data = request.get_json()
    number = data['number']
    json_text = voo_to_tax_limit(number)
    if json_text is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})
    else:
        return jsonify(json_text)


@app.route('/compra', methods=['POST']) # Compra
def compra():
    data = request.get_json()
    id_voo = data['id_voo']
    json_text = db_compra(id_voo)
    if json_text is None:
        return jsonify({'status': False, 'messagem': 'fall_conect_db'})
    else:
        return jsonify(json_text)

        
if __name__ == '__main__':
    #app.run(host='172.168.0.5',port=5000,debug=True)
    sess = Session()
    sess.init_app(app)
    app.run(debug=True)