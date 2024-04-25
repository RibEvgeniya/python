'''Вариант 12 Дан файл в формате csv. (Фамилия, Имя, Учреждение
(организация), Отдел, Адрес электронной почты, Состояние, Тест начат,
Завершено, Затраченное время, Оценка/100,00, В.1 /10,00, В.2 /10,00, В.3
/10,00, В.4 /10,00, В.5 /10,00, В.6 /10,00, В.7 /10,00, В.8 /10,00, В.9 /10,00, В.10
/10,00).
Примечание: Тест считается пройденным, если набрано 6/10 (60/100)
баллов.
Примечание: Поля «Тест начат», «Завершено» заданы в формате «12
Май 2017 10:09», поле «Затраченное время» в формате «31 мин. 22 сек.».
Вывести в алфавитном порядке слушателей, набравших заданное
количество баллов и выполнивших тест за наименьшее время.'''


import pandas as pd


def time_to_seconds(time_str):
    mas_time = []
    for item in time_str:
        time = item.replace(' мин.', '').replace(' сек.', '')
        print(time)
        minutes, seconds = map(int, time.split())
        mas_time.append(minutes * 60 + seconds)

    return pd.Series(mas_time)



data = pd.read_csv("12 - 1.csv")
pass_score = "6,00"
need_score="8,00"
min_time=0


result = data[time_to_seconds(data.get("Затраченное время",""))]
result = result[result.get("Оценка/10,00","") == need_score]
min_time=result["Затраченное время"].min
result = result[ result.get("Затраченное время","") == min_time]
print(len(result))
print(result.sort_values(by='Фамилия'))



data = pd.read_csv("12 - 2.csv")

result = data[time_to_seconds(data.get("Затраченное время",""))]
result = result[result.get("Оценка/10,00","") == need_score]
min_time=result["Затраченное время"].min
result = result[ result.get("Затраченное время","") == min_time]
print(len(result))
print(result.sort_values(by='Фамилия'))