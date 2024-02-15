# №1
#вариант 2
# Даны два списка чисел. Посчитайте, сколько чисел содержится
# одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.


n=int(input())
mass_1=[]
for i in range(0,n):
    x=int(input())
    mass_1.append(x)
mass_2=[]
for i in range(0,n):
    x=int(input())
    mass_2.append(x)
set_mass_1=set(mass_1)
set_mass_2=set(mass_2)
def common_elem(set_mass_1, set_mass_2):
    return len(set_mass_1 & set_mass_2)
print(common_elem(set_mass_1,set_mass_2))