# 12 вариант
# №1
# Найти сумму непростых делителей числа.
#x=int(input())
import random


def func_1(x):
    s=0
    for i in range(1,x):
        k=0
        if x%i==0:
            for j in range (1,i):
                if(i%j==0):
                    k+=1
        if k>1:
            s+=i
            print(i)
    return s
#print(func_1(x))

#Найти количество цифр числа, меньших 3
def func_2(x):
    k=0
    while x>1:
        m = x % 10
        x /= 10
        if m < 3:
            k += 1
    return k

#print(func_2(x))

#Найти количество чисел, не являющихся делителями
#исходного числа, не взамно простых с ним и взаимно простых с суммой
#простых цифр этого числа.
def func_31(x,i):
    if x%i!=0:
        return True
    return False

def func_32(x,i):
    k=0;
    for j in range(1,int(i)):
        if (x%j==0 and i%j==0):
            k+=1
    if k>1:
        return False
    return True

def func_33(x,i):
    s=0
    k = 0
    c=0
    while x > 1 and i>1:
        m = int(x % 10)
        x /= 10
        c=0
        for j in range(1,m):
            if m%j==0:
                c+=1
        if c==1:
            s+=int(m)
    if(x>s):
        return not(func_32(x,s))
    else:
        return not(func_32(s,x))

def func_3(x):
    for i in range (1,x):
        if func_31(x,i) and func_32(x,i) and func_33(x,i):
            print(i)



#func_3(x)




# №2-4



# 6 Дана строка в которой записаны слова через пробел. Необходимо
# перемешать в каждом слове все символы в случайном порядке кроме первого
# и последнего.
x=str(input())
s=x.split()
for i in range(0,len(s)):
    #print("word ", i+1)
    if len(s[i])>2:
        a=s[i]
        b=list(a[1:len(a)-1])
        random.shuffle(b)
        b="".join(b)
        #print(b)
        a=s[i][0]+b+s[i][len(s[i])-1]
        #print(a)
        s[i]="".join(a)

s=" ".join(s)
#print(s)

# 12 Дана строка в которой содержатся цифры и буквы. Необходимо
# расположить все цифры в начале строки, а буквы – в конце.

#s=list(x)
sa=""
sd=""
for i in range(0,len(s)):
    if s[i].isdigit():
        sa+=s[i]
    else:
        sd+=s[i]
s="".join(sa+sd)
#print(s)

# 13 Дана строка в которой записаны слова через пробел. Необходимо
# перемешать все слова в случайном порядке.

s=x.split()
random.shuffle(s)
s=" ".join(s)
#print(s)



# №5

# Дана строка. Необходимо найти все даты, которые описаны в
# виде "31 февраля 2007".
import re
#x=str(input())
s=re.findall(r'\d{1,2} \w{3,8} \d\d\d\d', x)
#print(s)


# №6-8

# 6 Дана строка. Необходимо подсчитать количество чисел в этой строке,
# значение которых больше 5

def func_6(x):
    s=x.split()
    k=0
    for i in range(0,len(s)):
        if s[i].isdigit():
            if int(s[i])>5:
                k+=1
    return k
#print(func_6(x))

# 12 Дана строка. Необходимо найти те символы кириллицы, которые не
# задействованы в данной строке.

def func_12(x):
    x=x.lower()
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    m=alph
    for i in range(0,len(x)):
        m=m.replace(x[i],"")
    return m
#print(func_12(x))

# 13 Дана строка. Необходимо найти максимальное из имеющихся в ней
# натуральных чисел.

def func_13(x):
    s = x.split()
    max=0
    for i in range(0, len(s)):
        if s[i].isdigit():
            if (int(s[i])) > max:
               max=int(s[i])
    return max
#print(func_13(x))



#  9 Прочитать список строк с клавиатуры. Упорядочить по длине
# строки.

def func_9(x):
    s = x.split()
    s.sort(key=len)
    return " ".join(s)
#print(func_9(x))


#Задание 10 Дан список строк с клавиатуры. Упорядочить по количеству
#слов в строке.


#n = int(input())
#x = []
#for i in range(n):
   # x.append(input())
def func_10(x,n):
    s=[]
    for i in range (0, n):
        s.append((x[i].split()).copy())
    s.sort(key=len)
    for i in range(0, n):
        s[i]=" ".join(s[i])
    return(s)
#print(func_10(x,n))



#-----------------------------------------------------------------------------------------------------------------------------
# №11-14


# 3 Отсортировать строки в указанном порядке В порядке увеличения разницы между частотой наиболее часто
# встречаемого символа в строке и частотой его появления в алфавите.


def poev_elem(x):
    alp='ESUKTHGXADYJOLPQNFWZRCBIMV'
    alp=alp.lower()
    ch='0.130 0.061	0.024 0.004 0.105 0.052	0.020 0.0015 0.081 0.038 0.019 0.0013 0.079	0.034 0.019	0.0011 0.071 0.029 0.015 0.0007	0.068 0.027	0.014 0.063	0.025 0.009'
    nch=ch.split()
    count=[]
    for i in range(0,len(x)):
        count.append(x.count(x[i]))
    maxim=max(count)
    for i in range(0,len(x)):
        if count[i]==maxim:
            elem=x[i]
    chastota_str=float(maxim/len(x))
    for i in range(0,len(alp)):
        if elem==alp[i]:
            chastota_alp=float(nch[i])
    razn=chastota_str-chastota_alp
    return razn

n = int(input())
x = []
for i in range(n):
    x.append(input())
def func_3(x,n):
    s=[]
    for i in range (0, n):
        s.append(x[i])
    for j in range(n - 1):
        for k in range(n - j - 1):
            if poev_elem(s[k]) > poev_elem(s[k + 1]):
                s[k], s[k + 1] = s[k + 1], s[k]
    for i in range(0, n):
        s[i]=" ".join(s[i])
    return(s)
#print(func_3(x,n))

# 6 Отсортировать строки в указанном порядке В порядке увеличения медианного значения выборки строк (прошлое
# медианное значение удаляется из выборки и производится поиск нового
# медианного значения).

def func_6(x,n):
    s=[]
    itog = []
    for i in range (0, n):
        s.append(x[i])
        s[i]=s[i].split()
    for i in range(0,n):
        spr = sorted(s[i])
        l=len(spr)
        if int(len(spr[i]) % 2) == 0:
            median = (spr[l / 2-1] + spr[l / 2 ]) / 2
        else:
            median = spr[int((l - 1) / 2)]
        itog.append([median, s[i]])
    itog = sorted(itog)
    for i in range(0, n):
        itog[i]=" ".join(itog[i][1])
    return(itog)
#print(func_6(x,n))


# 9 Отсортировать строки в указанном порядке В порядке увеличения квадратичного отклонения между наибольшим
# ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
# расположенных символов строки (относительно ее середины).


def func_9(x, n):
    s = []
    itog = []
    for i in range(0, n):
        s.append(x[i])
    for i in range(0,n):
        m=ord(max(s[i]))
        razn=0
        l=len(s[i])
        for j in range(0,int(l/2)):
            razn+=abs(ord(s[i][j])-ord(s[i][l-1-j]))
        itog.append([(m-razn)** 2, s[i]])
    itog = sorted(itog)
    for i in range(0, n):
        itog[i] = " ".join(itog[i][1])
    return itog
#print(func_9(x, n))

# 10 Отсортировать строки в указанном порядке В порядке увеличения среднего количества «зеркальных» троек
# (например, «ada») символов в строке.

def func_10(x, n):
    s = []
    for i in range(n):
        c = 0
        for j in range(len(x[i]) - 2):
            if x[i][j] == x[i][j + 2]:
                c += 1
        s.append([c, x[i]])
    s = sorted(s)
    for i in range(0, n):
        s[i] = " ".join(s[i][1])
    return s

#print(func_10(x, n))





