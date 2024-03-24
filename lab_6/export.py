import sqlite3
import json
data = []

def addData(tablename):
    con = sqlite3.connect('db_insurance_company.db')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tablename}")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    con.close()
    return data
data.append(addData("Client"))
data.append(addData("Branch"))
data.append(addData("Employee"))
data.append(addData("Contract"))
with open('developers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)