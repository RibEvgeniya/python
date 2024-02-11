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

