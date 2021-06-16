from datetime import date
import psycopg2

class ClientDB():
    def __init__(self,user=None,email=None,password=None):
        self.user = user
        self.pasw = password
        self.email = email
        #self.mypoll = self.connect()
        self.pesquisa = {}

    def connect(self):
        return psycopg2.connect("dbname=aero user=postgres password=8833xxxx")

    #def disconnect(self):
    #    self.

    def get_user(self):
        return self.user

    def get_pass(self):
        return self.pasw

    def get_email(self):
        return self.email

    def set_user(self,user):
        self.user = user

    def set_pass(self,password):
        self.pasw = password

    def set_email(self,email):
        self.email = email
        
    def is_pesquisa(self,key):
        for content in self.pesquisa:
            if content == key:
                return self.pesquisa[key]
            else:
                return False
            
    def user_get_pass(self):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                if self.user is not None:
                    cur.execute(
                        "SELECT password FROM tb_user WHERE linkname=%s",
                        (self.user,))
                    
                    r = cur.fetchone()
                    if r is None:
                        return []
                    for record in r:
                        results.append(record)
                    conn.commit()
        return results


    def user_get_email(self):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                if self.user is not None:
                    cur.execute(
                        "SELECT email FROM tb_user WHERE linkname=%s",
                        (self.user,))
                   
                    r = cur.fetchone()
                    if r is None:
                        return []
                    for record in r:
                        results.append(record)
                    conn.commit()
        return results

    def email_get_user(self):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                if self.email is not None:
                    cur.execute(
                        "SELECT linkname FROM tb_user WHERE email=%s",
                        (self.email,))

                    r = cur.fetchone()
                    if r is None:
                        return []
                    for record in r:
                        results.append(record)
                    cnn.commit()
        return results

    def email_get_pass(self):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                if self.email is not None:
                    cur.execute(
                        "SELECT password,linkname FROM tb_user WHERE email=%s",
                        (self.email,))

                    r = cur.fetchone()
                    if r is None:
                        return []
                    for record in r:
                        results.append(record)
                    cnn.commit()
        return results

    def nda_none(self):
        if self.user is not None and \
           self.email is not None and \
           self.pasw is not None:
            return True
        else:
            return False

    def insert_user(self):
        user_db = email_get_user()
        if user_db[0] == self.user:
            return False
        elif self.nda_none:
            with self.connect() as cnn:
                with cnn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO tb_user (linkname,email,password) VALEUS (%s, %s, %s)",
                        (self.user,self.email,self.pasw))
                    cnn.commit()
            return True
        else:
            return False
                        

    def getall_voo_to_id_voo(self,id_voo):
        results = []
        #ja_pesquisado = self.is_pesquisa(id_voo)
        #if not ja_pesquisado:
        #    return ja_pesquisado
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_voo WHERE id_voo=%s",(id_voo,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)

                cnn.commit()

        return results
        
    def getall_voo_to_origem(self,origem):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_voo WHERE origem=%s", (origem,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)

                cnn.commit()
        return results

    def getall_voo_to_destino(self,destino):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_voo WHERE destino=%s", (destino,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)

                cnn.commit()
        return rwesults

    def getall_voo_to_companhia(self,companhia):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_voo WHERE companhia=%s", (companhia,))
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)
                cnn.commit()
        return results

    
    def getall_aero_to_nome(self,nome):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_aeropostos WHERE nome=%s", (nome,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)
                cnn.commit()
        return results

    def getall_areo_to_cidade(self,cidade):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_aeropostos WHERE cidade=%s", (cidade,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)

                cnn.commit()
        return results

    def getall_aero_to_estado(self,estado):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_aeropostos WHERE estado=%s", (estado,))
                
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)
                cnn.commit()
        return results


    def getall_areo_to_sigla(self,sigla):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tb_aeropostos WHERE sigla=%s", (sigla,))
                r = cur.fetchone()
                if r is None:
                    return []
                for record in r:
                    results.append(record)

                cnn.commit()
        return results

    
    def get_preco_to_id_voo(self,id_voo):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT precos,total_vagas,disponiveis FROM tb_precos WHERE id_voo=%s",
                    (id_voo,))
                r = cur.fetchone()
                if r is None:
                    return None
                for record in r:
                    results.append(record)

                cnn.commit()
        
        return results

    def get_voo_to_src_dst(self,origem,destino):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT id_voo FROM tb_voo WHERE origem=%s and destino=%s",
                    (origem,destino,))

                r = cur.fetchone()
                if r is None:
                    return None
                for record in r:
                    results.append(record)
                cnn.commit()

        return results

    def get_vagas_to_id_voo(self,id_voo):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "SELECT total_vagas, disponiveis FROM tb_precos WHERE id_voo=%s",
                    (id_voo,))
                
                r = cur.fetchone()
                if r is None:
                    return None
                for record in r:
                    results.append(record)

                cnn.commit()
        return results

    def get_voo_to_day(self,day,mes,ano,day2=None,mes2=None,anos2=None):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                if day2 is not None and mes2 is not None and anos2 is not None:
                    cur.execute(
                        "SELECT id_voo,companhia FROM tb_voo WHERE data_voo BETWEEN %s and %s",
                        (date(ano,mes,day).isoformat(),
                         date(ano2,mes2,day2).isoformat(),))
                else:
                    cur.execute(
                        "SELECT id_voo,companhia FROM tb_voo WHERE data_voo BETWEEN %s and now()",
                        (date(ano,mes,day).isoformat(),))
                        
                
                r = cur.fetchone()
                if r is None:
                    return None
                for record in r:
                    results.append(record)

                cnn.commit()
        return results

    def get_voo_to_minus_tarifas(self,number):
        results = []
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id_voo,origem,destino,companhia FROM tb_voo 
                    ORDER BY tax1p ASC LIMIT %s
                    """, (number,))
                
                r = cur.fetchone()
                if r is None:
                    return None
                for record in r:
                    results.append(record)

                cnn.commit()

        return results
    
    
    def update_voo_one(self,id_voo,disponivel):
        with self.connect() as cnn:
            with cnn.cursor() as cur:
                cur.execute(
                    "UPDATE tb_precos SET disponiveis=%s WHERE id=%s",(disponivel,id_voo))
        return None
                    
    
        
    
