# №1
#вариант 2
# Даны два списка чисел. Посчитайте, сколько чисел содержится
# одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.


#n=int(input())
#mass_1=[]
#for i in range(0,n):
    #x=int(input())
    #mass_1.append(x)
#mass_2=[]
#for i in range(0,n):
    #x=int(input())
    #mass_2.append(x)
#set_mass_1=set(mass_1)
#set_mass_2=set(mass_2)
def common_elem(set_mass_1, set_mass_2):
    return len(set_mass_1 & set_mass_2)
#print(common_elem(set_mass_1,set_mass_2))


# №2
# вариант 12
#В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
#Каждом элементу дерева сопоставляется целое неотрицательное число,
#называемое высотой. У родоначальника высота равна 0, у любого другого
#элемента высота на 1 больше, чем у его родителя.
#Вам дано генеалогическое древо.
#Программа получает на вход число элементов в генеалогическом древе
#N . Далее следует N −1 строка, задающие родителя для каждого элемента
#древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
#Даны два элемента в дереве. Определите, является ли один из них
#потомком другого.
#Во входных данных записано дерево в том же формате, что и в
#предыдущей задаче Далее идет число запросов K . В каждой из следующих K
#строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый
# элемент является предком второго, 2, если второй является предком первого
# или 0, если ни один из них не является предком другого.


n=int(input())
tree=dict()
for n in range (0,n-1):
    x=input().split()
    tree[x[0]]=x[1]
check=[]
m = int(input())
for n in range(0, m):
    check.append(input())
def is_somewhat_ancestor(tree,child,ancestor):
    if(child==ancestor):
        return True
    while child in tree:
        child = tree[child]
        if child == ancestor:
            return True
    return False

def func_tree(tree,check):
    for i in range(0, m):
        line=check[i]
        spl_line=line.split()
        child = spl_line[0]
        ancestor = spl_line[1]
        if (is_somewhat_ancestor(tree,child,ancestor)):
            print(2)
        elif (is_somewhat_ancestor(tree,ancestor, child)):
            print(1)
        else:
            print( 0)

func_tree(tree,check)