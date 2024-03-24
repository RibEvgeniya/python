import sqlite3
import datetime

con=sqlite3.connect('db_insurance_company.db')

cur = con.cursor()
command='''CREATE TABLE IF NOT EXISTS Client
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        surname VARCHAR(30) NOT NULL,
        name VARCHAR(30) NOT NULL,
        patronymic VARCHAR(30) NOT NULL,
        phone VARCHAR(11) NOT NULL);'''
cur.execute(command)
command='''CREATE TABLE IF NOT EXISTS Branch
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(30) NOT NULL,
        city VARCHAR(30) NOT NULL,
        adress VARCHAR(30) NOT NULL,
        phone VARCHAR(11) NOT NULL);'''
cur.execute(command)
command='''CREATE TABLE IF NOT EXISTS Employee
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        surname VARCHAR(30) NOT NULL,
        name VARCHAR(30) NOT NULL,
        patronymic VARCHAR(30) NOT NULL,
        gender VARCHAR(11) NOT NULL,
        phone VARCHAR(11) NOT NULL,
        branch_id INTEGER,
        FOREIGN KEY (branch_id) REFERENCES Branch(id));'''
cur.execute(command)
command='''CREATE TABLE IF NOT EXISTS Types_of_insurance
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(30) NOT NULL,
        procent INTEGER NOT NULL);'''
cur.execute(command)

command='''CREATE TABLE IF NOT EXISTS Contract
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(30) NOT NULL,
        date TIMESTAMP NOT NULL,
        insurance_summ REAL NOT NULL,
        insurance_payment REAL NOT NULL,
        branch_id INTEGER,
        employee_id INTEGER,
        client_id INTEGER,
        type_ins_id INTEGER,
        object VARCHAR(30) NOT NULL,
        FOREIGN KEY(branch_id) REFERENCES Branch(id),
        FOREIGN KEY(employee_id) REFERENCES Employee(id),
        FOREIGN KEY(client_id) REFERENCES Client(id),
        FOREIGN KEY(type_ins_id) REFERENCES Types_of_insurance(id) );'''
cur.execute(command)

con.commit()

con.close()