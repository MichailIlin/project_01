# Задача 2.1. 

# Создайте две функции maximum и maximum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    if len(arr)>0:
        mn=arr[0]
        for i in arr:
            if i<mn:
                mn=i
        return mn
    else: return None

def maximum(arr):
    if len(arr)>0:
        mX=arr[0]
        for i in arr:
            if i>mX:
                mX=i
        return mX
    else: return None

print('minimum')
print(minimum([4,6,2,1,9,63,-134,566]))
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(minimum([42, 54, 65, 87, 0]))
print(minimum([5]))
print()
print('maximum')
print(maximum([4,6,2,1,9,63,-134,566]))
print(maximum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([42, 54, 65, 87, 0]))
print(maximum([5]))