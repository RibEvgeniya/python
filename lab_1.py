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
x=str(input())
s=re.findall(r'\d{1,2} \w{3,8} \d\d\d\d', x)
print(s)


