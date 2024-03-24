
import cgi
import cgitb
import html
import sqlite3
print("Content-type: text/html\n")


cgitb.enable()

form =cgi.FieldStorage()
text1 = form.getfirst("date","не задано")
text2 = form.getfirst("insurance_summ", "не задано")
text3 = form.getfirst("insurance_payment", "не задано")
text4 = form.getfirst("branch_id1", "не задано")
text5 = form.getfirst("employee_id", "не задано")
text6 = form.getfirst("client_id", "не задано")
text7 = form.getfirst("object", "не задано")
text8 = form.getfirst("name_of_insurance", "не задано")
text1=html.escape(text1)
text2=html.escape(text2)
text3=html.escape(text3)
text4=html.escape(text4)
text5=html.escape(text5)
text6=html.escape(text6)
text7=html.escape(text7)
text8=html.escape(text8)
try:
    conn = sqlite3.connect('db_insurance_company.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Contract (date, insurance_summ,insurance_payment,branch_id1,employee_id,client_id,object,name_of_insurance) 
                      VALUES ( ?, ?, ?, ?,?,?,?,?)''', (text1, text2, text3,text4,text5,text6,text7,text8))
    conn.commit()
    print('<html>')
    print('<head>')
    print('<title> Python on a web server</title>')
    print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')
    print(' <meta name="viewport" content="width=device-width initial-scale=1,shrink-to-fit=no">')
    print('<link rel="stylesheet" href="style.css">')
    print('</head>')
    print('<body>')

    print('<h2>Новый договор:</h2>', '<br /><br />')
    print('</body>')
    print('</html>')
    print("<p>Дата заключения:", text1)
    print("<p>Сумма страхования:", text2)
    print("<p>Оплата страхования:", text3)
    print("<p>ID филиала:", text4)
    print("<p>ID сотрудника:", text5)
    print("<p>ID клиента:", text6)
    print("<p>Объет для страхования:", text7)
    print("<p>Вид страхования:", text8)
    print ('</body>')
    print ('</html>')
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()