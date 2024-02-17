# №1
#вариант 2
#Менеджер по работе с персоналом присваивает рейтинговый балл каждому из N кандидатов, резюме которых он изучает. Он хочет нанять двух
#специалистов с суммарным рейтингом не менее К баллов. Требуется по имеющимся данным о баллах N кандидатов определить, сколько различных
#пар кандидатов можно выбрать так, чтобы их суммарный рейтинговый балл составлял не менее К. Две пары кандидатов считаются различными, если хотя
#бы один из членов пары не присутствует в другой паре. Запишите в ответе найденное количество пар.
f = open('27-169a.txt', 'r')
g = open('res.txt', 'w')
line=((f.readline()).split())
n,k=int(line[0]),int(line[1])
m=[int(x) for x in f]
count=0
sorted(m)
left=0
right=n-1
for i in range (n):
    if(m[left]+m[right]>=k):
        count+=right-left
        right-=1
    else:
        left+=1

g.write(str(count))
print(count)
f.close()
g.close()


# №2
#вариант 12
#Дан файл, содержащий зашифрованный русский текст. Каждая буква заменяется на следующую за ней (буква я заменяется на а). Получить в новом файле расшифровку данного текста.

f2 = open('code_file.txt', 'r', encoding='utf-8')
g2 = open('decode_file.txt', 'w')

alph='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text=f2.read()
text=text.lower()
res=''
for i in text:
    if(i.isalpha()):
        index=alph.find(i)
        #res += alph[(index + 1)%33]
        if(index==0):
            res+=alph[32]
        else:
            res+=alph[(index-1)]
    else:
        res+=i
print(res)
g2.write(res)
f2.close()
g2.close()

