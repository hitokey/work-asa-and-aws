FROM ubuntu
#USEI A IMAGEM DO UBUNTU, PORQUE ELA E PEQUENA

RUN apt update && apt install python3 python3-pip -y
RUN apt install libpq5

RUN pip3 install flask
RUN pip3 install psycopg3

#ENV FLASK_ENV=development

COPY ["application/.", "/home/."]
COPY ["application/src/.", "/home/src/."]
COPY ["aplication/db/.", "/home/db/."]

EXPOSE 5000

CMD ["python3", "/home/web_api.py"]

#ENTRYPOINT python3 /home/app.py
#TESTE: IMAGEM
#docker image build -t pythonflask:latest .
#docker run -d --name flask -p 5000:5000 pythonflask