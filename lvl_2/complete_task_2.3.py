# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# def switch_it_up_1(number):
#     ls=['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
#     if 0<=number<=9:
#         return ls[number]
#     else: return "Ошибка"

#Вариант 1
def switch_it_up(number):
    match number:
        case 0:
            return 'ноль'
        case 1:
            return 'один'
        case 2:
            return 'два'
        case 3:
            return 'три'
        case 4:
            return 'четыре'
        case 5:
            return 'пять'
        case 6:
            return 'шесть'
        case 7:
            return 'семь'
        case 8:
            return 'восемь'
        case 9:
            return 'девять'
        case _:
            return "Ошибка"

#Вариант 2    
def switch_it_up_1(number):
     ls=('ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять')
     try:
         return ls[number]
     except: 
         return "Ошибка"

print()    
print('Вариант 1')    
for i in range(0,11):  
    k=switch_it_up(i)
    print(i,k)
print()
print('Вариант 2')
for i in range(0,11):  
    k=switch_it_up_1(i)
    print(i,k)