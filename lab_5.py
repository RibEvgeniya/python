# №1
#вариант 2
#Реализовать функцию, которая будет проверять, является ли введенная строка IP-адресом (v4), возвращаемое значение True или False.
#Дополнительно реализовать функцию, которая выбрасывает исключение о некорректном аргументе, иначе возвращает IP-адрес (v4).
import re


ip0="245.4.53.12"
ip1="245.04.53.12"
ip2="265.4.5.121"

def is_valid(ip):
    pat = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9] ?)\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9] ?)$")
    test = pat.match(ip)
    if test:
        return True
    return False

def check_valid(ip):
    try:
        if is_valid(ip):
            print(ip)
        else:
            raise Exception('ip error')
    except Exception:
        print('Wrong ip!', ip, 'cannot exists')

check_valid(ip0)
check_valid(ip1)
check_valid(ip2)
