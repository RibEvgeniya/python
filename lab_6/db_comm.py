import sqlite3
import datetime

con=sqlite3.connect('db_insurance_company.db')

cur = con.cursor()


command='''CREATE TABLE IF NOT EXISTS Client
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        surname VARCHAR(30) NOT NULL,
        name VARCHAR(30) NOT NULL,
        patronymic VARCHAR(30) NOT NULL,
        phone VARCHAR(12) NOT NULL);'''
cur.execute(command)
command='''CREATE TABLE IF NOT EXISTS Branch
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(30) NOT NULL,
        city VARCHAR(30) NOT NULL,
        adress VARCHAR(30) NOT NULL,
        phone VARCHAR(12) NOT NULL);'''
cur.execute(command)
command='''CREATE TABLE IF NOT EXISTS Employee
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        surname VARCHAR(30) NOT NULL,
        name VARCHAR(30) NOT NULL,
        patronymic VARCHAR(30) NOT NULL,
        gender VARCHAR(11) NOT NULL,
        phone VARCHAR(12) NOT NULL,
        branch_id INTEGER,
        FOREIGN KEY (branch_id) REFERENCES Branch(id));'''
cur.execute(command)


command='''CREATE TABLE IF NOT EXISTS Contract
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        date TIMESTAMP NOT NULL,
        insurance_summ REAL NOT NULL,
        insurance_payment REAL NOT NULL,
        branch_id INTEGER,
        employee_id INTEGER,
        client_id INTEGER,
        object VARCHAR(30) NOT NULL,
        name_of_insurance VARCHAR(30) NOT NULL,
        FOREIGN KEY(branch_id) REFERENCES Branch(id),
        FOREIGN KEY(employee_id) REFERENCES Employee(id),
        FOREIGN KEY(client_id) REFERENCES Client(id) );'''
cur.execute(command)

con.commit()


command='''INSERT INTO Client 
   VALUES(NULL, 'Иванов','Иван', 'Иванович', '+79188888888');'''
cur.execute(command)
command='''INSERT INTO Client 
   VALUES(NULL, 'Иванова','Иванна', 'Ивановна', '+79299999999');'''
cur.execute(command)
command='''INSERT INTO Client 
   VALUES(NULL, 'Серов','Сергей', 'Юрьевич', '+79181234567');'''
cur.execute(command)


command='''INSERT INTO Branch 
   VALUES(NULL, 'Первый','Краснодар', 'улица Ставропольская 1', '+79111111111');'''
cur.execute(command)
command='''INSERT INTO Branch 
   VALUES(NULL, 'Второй','Москва', 'улица Вторая 1', '+11111111111');'''
cur.execute(command)
command='''INSERT INTO Branch 
   VALUES(NULL, 'Третий','Краснодар', 'улица Ставропольская 3', '+79111111122');'''
cur.execute(command)

command='''INSERT INTO Employee
   VALUES(NULL, 'Куськова','Мария', 'Сергеевна','Женский', '+79188888888','0');'''
cur.execute(command)
command='''INSERT INTO Employee
   VALUES(NULL, 'Куськова','Наталья', 'Сергеевна','Женский', '+79199887765','1');'''
cur.execute(command)
command='''INSERT INTO Employee
   VALUES(NULL, 'Мыхин','Юрий', 'Олегов','Мужской', '+7894536354','0');'''
cur.execute(command)


command='''INSERT INTO Contract
   VALUES(NULL,'2019-06-28','3000000','40000','0','1','1','машина', 'имущественное');'''
cur.execute(command)
command='''INSERT INTO Contract
   VALUES(NULL,'2020-03-08','5000000','60000','2','0','0','квартира', 'имущественное');'''
cur.execute(command)
command='''INSERT INTO Contract
   VALUES(NULL,'2020-11-01','7000000','70000','1','2','1','дом', 'имущественное');'''
cur.execute(command)
con.commit()



con.close()