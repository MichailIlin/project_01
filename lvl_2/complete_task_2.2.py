# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.
months=('январь','февраль','март','апрель','май','июнь','июль','август','сентябрь',
     'октябрь','ноябрь','декабрь')
quarta=('первого','второго','третьего','четвертого')
def quarter_of(month):
    if 0<month<13:
        if month<4:
            rs=1
        elif month<7:
            rs=2
        elif month<10:
            rs=3
        else: rs=4
    else: rs=0
    return rs

print()
print('*'*10,'Func quarter','*'*10)
for i in range(1,13):
    q=quarter_of(i)
    if q>0:
        print(f'месяц {i} ({months[i-1]}) является частью {quarta[q-1]} квартала')
    else:
        print('Неправильный номер месяца')

