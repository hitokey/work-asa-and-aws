CREATE TABLE tb_aeropostos(
       id SERIAL PRIMARY KEY,
       nome VARCHAR(255),
       cidade VARCHAR(255),
       estado VARCHAR(255),
       sigla VARCHAR(255)
);

CREATE TABLE tb_voo(
       id_voo SERIAL PRIMARY KEY,
	   id_aero INTEGER NOT NULL,
       origem VARCHAR(255),
       destino VARCHAR(255),
       companhia VARCHAR(255),
       tax1p FLOAT,
       data_voo DATE,
       hora_voo TIME,
	   CONSTRAINT fk_id FOREIGN KEY(id_aero)
       		  REFERENCES tb_aeropostos(id)
);

CREATE TABLE tb_precos(
       id SERIAL PRIMARY KEY,
       id_voo INT NOT NULL,
       precos FLOAT,
       total_vagas INT,
       disponiveis INT,
       CONSTRAINT fk_id FOREIGN KEY(id_voo)
       		  REFERENCES tb_voo(id_voo)
);
       

CREATE TABLE tb_user(
       id SERIAL PRIMARY KEY,
       linkname VARCHAR(255),
       email VARCHAR(255),
       password VARCHAR(255)
);	


INSERT INTO tb_aeropostos(nome,cidade,estado,sigla) VALUES('AERO1', 'UBERLANDIA','MINAS GERAIS', 'MG');
INSERT INTO tb_aeropostos(nome,cidade,estado,sigla) VALUES('AERO2','RIO JANEIRO','RIO JANEIRO', 'RJ');
INSERT INTO tb_aeropostos(nome,cidade,estado,sigla) VALUES('AERO3','SÃO PAULO','SÃO PAULO', 'SP');

SELECT * FROM tb_aeropostos;
SELECT * FROM tb_aeropostos WHERE nome='AERO1';
SELECT * FROM tb_aeropostos WHERE cidade='SÃO PAULO';
SELECT * FROM tb_aeropostos WHERE estado='MINAS GERAIS';
SELECT * FROM tb_aeropostos WHERE sigla='MG'

/*
INSERT INTO  tb_voo(id_aero,origem,destino,companhia,tax1p,data_voo,hora_voo)
			 VALUES(1,'UBERLANDIA','RIO JANEIRO','COMP1',70.00,'10/10/2021','19:30');
			 
INSERT INTO  tb_voo(id_aero,origem,destino,companhia,tax1p,data_voo,hora_voo)
			 VALUES(1,'UBERLANDIA','SÃO PAULO','COMP1',70.00,'10/10/2021','19:30');

INSERT INTO  tb_voo(id_aero,origem,destino,companhia,tax1p,data_voo,hora_voo)
			 VALUES(2,'RIO JANEIRO','SÃO PAULO','COMP2',70.00,'10/10/2021','19:30');

INSERT INTO  tb_voo(id_aero,origem,destino,companhia,tax1p,data_voo,hora_voo)
			 VALUES(1,'UBERLANDIA','SÃO PAULO','COMP2',70.00,now(),'19:30');

SELECT * FROM tb_voo;
SELECT * FROM tb_voo WHERE id_voo=1
SELECT * FROM tb_voo WHERE origem='RIO JANEIRO'
SELECT * FROM tb_voo WHERE destino='SÃO PAULO'
SELECT * FROM tb_voo WHERE companhia='COMP2'
SELECT id_voo FROM tb_voo WHERE origem='RIO JANEIRO' and destino='SÃO PAULO';
SELECT id_voo,companhia FROM tb_voo WHERE data_voo BETWEEN '2021-01-01' and '2021-10-30';
SELECT id_voo,companhia FROM tb_voo WHERE data_voo BETWEEN '2021-01-01' and now();
SELECT id_voo,origem,destino,companhia FROM tb_voo ORDER BY tax1p ASC LIMIT 2;

INSERT INTO tb_precos(id_voo,precos,total_vagas,disponiveis) VALUES(1,1970,42,30);
INSERT INTO tb_precos(id_voo,precos,total_vagas,disponiveis) VALUES(2,2970,42,35);
INSERT INTO tb_precos(id_voo,precos,total_vagas,disponiveis) VALUES(3,970,42,42);

SELECT * FROM tb_precos;
SELECT precos,total_vagas,disponiveis FROM tb_precos WHERE id_voo=2;
SELECT total_vagas, disponiveis FROM tb_precos WHERE id_voo=2;
SELECT disponiveis FROM tb_precos WHERE id_voo=%s

INSERT INTO tb_user(linkname,email,password) VALUES('USER1','user1@email','1234');
INSERT INTO tb_user(linkname,email,password) VALUES('USER2','user2@email','1234');

SELECT * FROM tb_user;
SELECT password FROM tb_user WHERE email='user1@email';
SELECT linkname FROM tb_user WHERE email='user2@email';
SELECT email FROM tb_user WHERE linkname='USER1';
SELECT password FROM tb_user WHERE linkname='USER2';

UPDATE tb_precos SET id_voo=3 WHERE id=3;
UPDATE tb_aeropostos SET sigla='RJ' WHERE id=2;
UPDATE tb_aeropostos SET sigla='SP' WHERE id=3;
DROP TABLE if exists tb_voo cascade;
UPDATE tb_precos SET disponiveis=36 WHERE id=2

SELECT id_voo,origem,destino,companhia FROM tb_voo ORDER BY tax1p ASC LIMIT 3;
*/