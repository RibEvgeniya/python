
import cgi
import cgitb
import html
import sqlite3
print("Content-type: text/html\n")


cgitb.enable()

form =cgi.FieldStorage()
text1 = form.getfirst("name_emp","не задано")
text2 = form.getfirst("surname_emp", "не задано")
text3 = form.getfirst("patronymic_emp", "не задано")
text4 = form.getfirst("phone_emp", "не задано")
text5 = form.getfirst("gender", "не задано")
text6 = form.getfirst("branch_id", "не задано")
text1=html.escape(text1)
text2=html.escape(text2)
text3=html.escape(text3)
text4=html.escape(text4)
text5=html.escape(text5)
text6=html.escape(text6)
try:
    conn = sqlite3.connect('db_insurance_company.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Employee (name, surname, patronymic,phone,gender,branch_id) 
                      VALUES ( ?, ?, ?, ?,?,?)''', (text1, text2, text3,text4,text5,text6))
    conn.commit()
    print('<html>')
    print('<head>')
    print('<title> Python on a web server</title>')
    print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')
    print(' <meta name="viewport" content="width=device-width initial-scale=1,shrink-to-fit=no">')
    print('<link rel="stylesheet" href="style.css">')
    print('</head>')
    print('<body>')

    print('<h2>Новый работник:</h2>', '<br /><br />')
    print('</body>')
    print('</html>')
    print("<p>Имя:", text1)
    print("<p>Фамилия:", text2)
    print("<p>Отчество:", text3)
    print("<p>Телефон:", text4)
    print("<p>Пол:", text5)
    print("<p>ID филиала:", text6)
    print ('</body>')
    print ('</html>')
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()