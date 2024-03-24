import json

with open("developers.json", 'r', encoding='UTF-8') as f:
 data = json.load(f)
for i in data:
    print("Данные новой таблицы")
    for j in i:
        print(j)