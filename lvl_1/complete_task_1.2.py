# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 



#Если время время в песнях представляет собой минуты в виде вешественного числа
#то тогда см текущий вариант

#Если же имелось ввиду, что, например, 4.25 это 4 мин и 25сек, 
# тогда нужно раскомментировать др вариант

#'Задача 1.2 пункт A и C'
print('Задача 1.2 пункт A и C')
ls=[random.choice(my_favorite_songs) for i in range(0,3)]
print(f'randon select: ',ls)
total=0
for i in ls:
    total+=i[1]
print(f'Три песни звучат {total:.2f} минуты')
print()

#'Задача 1.2 пункт B и C'
print('Задача 1.2 пункт B и C')
keys=list(my_favorite_songs_dict.keys())
ls=[random.choice(keys) for i in range(0,3)]
print(f'random select:',ls)
total=0
for i in ls:
    total+=my_favorite_songs_dict[i]
print(f'Три песни звучат {total:.2f} минуты')
print()

#'Задача 1.2 пункт C'
print('Задача 1.2 пункт C')
ls=[random.choice(my_favorite_songs) for i in range(0,3)]
print(f'randon select: ',ls)
print()

#'Задача 1.2 пункт D'
print('Задача 1.2 пункт D')
ls=[random.choice(my_favorite_songs) for i in range(0,3)]
print(f'randon select: ',ls)
total=0
for i in ls:
    total+=i[1]*60
m,s=divmod(round(total),60)
tm=datetime.time(minute=int(m),second=int(s))
print(f'Три песни звучат {tm} минуты')
print()

#print('Задача 1.2 пункт A и C')
# ls=[random.choice(my_favorite_songs) for i in range(0,3)]
# print(f'randon select: ',ls)
# total=0
# for i in ls:
#     m,s=divmod(i[1],1)
#     total=total+m*60+s*100
# m,s=divmod(total,60)   
# print(f'Три песни звучат {m+round(s/100,3)}')
# print()

#print('Задача 1.2 пункт B и C')
# keys=list(my_favorite_songs_dict.keys())
# ls=[random.choice(keys) for i in range(0,3)]
# print(f'random select:',ls)
# total=0
# for i in ls:
#     m,s=divmod(my_favorite_songs_dict[i],1)
#     total=total+m*60+s*100
# m,s=divmod(total,60)   
# print(f'Три песни звучат {m+round(s/100,3)}')
# print()

#'Задача 1.2 пункт C'
# print('Задача 1.2 пункт C')
# ls=[random.choice(my_favorite_songs) for i in range(0,3)]
# print(f'randon select: ',ls)
# print()

#'Задача 1.2 пункт D'
print('Задача 1.2 пункт D')
ls=[random.choice(my_favorite_songs) for i in range(0,3)]
print(f'randon select: ',ls)
total=0
for i in ls:
    m,s=divmod(i[1],1)
    total=total+m*60+s*100
m,s=divmod(total,60)
tm=datetime.time(minute=int(m),second=int(s))
print(f'Три песни звучат {tm} минуты')
print()