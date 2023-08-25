# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
from datetime import datetime
from calendar import monthrange, month_name


my_month={
    '1': ('январь',31),
    '2': ('февраль',28),
    '3': ('март',31),
    '4': ('апрель',30),
    '5': ('май',31),
    '6': ('июнь',30),
    '7': ('июль',31),
    '8': ('август',31),
    '9': ('сентябрь',30),
    '10': ('октябрь',31),
    '11': ('ноябрь',30),
    '12': ('декабрь',31),
}
print()
print('Вариант 1')
mn=input('Введите номер месяца:')
if mn in my_month:
    if my_month[mn][1]==31:
        s='день'
    else:
        s='дней'
    print(f'Вы ввели {my_month[mn][0]} {my_month[mn][1]} {s}')
else:
    print('Вы ввели либо неправильный номер месяца, либо не число')
print()

print('Вариант 2')
i=int(mn)
if 0<i<13:
    current_year = datetime.now().year
    mns=list(month_name)
    days = monthrange(current_year, i)
    if days[1]==31:
        s='день'
    else:
        s='дней'                      
    print(f'Вы ввели {mns[i]} {days[1]} {s}')
else:
    print('Вы ввели либо неправильный номер месяца, либо не число')
