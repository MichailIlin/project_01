# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, 
# второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print('Вариант 0')
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(my_favorite_songs[0:14])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-26:-15])

print('Вариант 1')
mfs=my_favorite_songs #только, чтобы не писать длинное имя переменной

ls=[]
for i in range(0,len(mfs)):
    if mfs[i]==',':
        ls.append(i)
i=len(ls)
if i>2:
    print(mfs[0:ls[0]])
    print(mfs[ls[i-1]+1:])
    print(mfs[ls[0]+1:ls[1]])
    print(mfs[ls[i-2]+1:ls[i-1]])
else:
    print('Ошибка')
    
# print('Вариант 1a')
# ls=[i for i in range(0,len(mfs)) if mfs[i]==',']
# print(mfs[0:ls[0]])
# print(mfs[ls[i-1]+1:])
# print(mfs[ls[0]+1:ls[1]])
# print(mfs[ls[i-2]+1:ls[i-1]])

print('Вариант 2')
i=mfs.find(',')
print(mfs[0:i])
s=mfs[i+1:]
j=s.find(',')
i=mfs.rfind(",")
print(mfs[i+1:len(mfs)])
print(s[0:j])
s=mfs[0:i]
i=s.rfind(',')
print(s[i+1:len(s)])

print('Вариант 3')
ls=mfs.split(',')
i=len(ls)
if i>2:
    print(ls[0])
    print(ls[i-1])
    print(ls[1])
    print(ls[i-2])
else:
    print('Ошибка')

