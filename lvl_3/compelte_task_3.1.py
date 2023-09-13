# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)
import random
class Matrix:
    def __init__(self,arow,acol):
        self.row=arow
        self.col=acol
        self.mat=[]
        # for i in range(arow):
        #     self.mat.append([0 for j in range(acol)])
        self.mat=[[None for j in range(acol)] for i in range(arow)]

    def __str__(self) -> str:
        '''Выводит на экран матрицу'''
        s=''
        for i in range(self.row):
            for j in range(self.col):
                s=s+str(self.mat[i][j]).ljust(5)
            s=s+'\n'
        return s
    
    def __eq__(self, other):
        ''' равенство матриц'''
        res=False
        if isinstance(other, type(self)) and self.row==other.row and self.col==other.col:
            res=True
            i=0
            while i<self.row and res:
                j=0
                while j<self.col and res:
                    res= self.mat[i][j]==other.mat[i][j]
                    j+=1
                i+=1
        return res
    
    def __add__(self,other):
        ''' Сложенеи матриц'''
        res=None
        if isinstance(other, type(self)) and self.row==other.row and self.col==other.col:
            mt=Matrix(self.row,self.col)
            for i in range(self.row):
                for j in range(self.col):
                    n=self.mat[i][j]
                    m=other.mat[i][j]
                    match n,m:
                        case (None,None):
                            mt.mat[i][j]=None
                        case (n,None):
                            mt.mat[i][j]=self.mat[i][j]
                        case (None,m):
                            mt.mat[i][j]=other.mat[i][j]
                        case _:
                            if type(self.mat[i][j])==type(other.mat[i][j]):
                                mt.mat[i][j]=self.mat[i][j]+other.mat[i][j]
                            else:
                                mt.mat[i][j]=None
        return mt

    
    
    def randomval(self,aval):
        '''Заполняет матрицу случайными значениями до aval и случайным образом пропускает некоторые ячейки'''
        for i in range(self.row):
            for j in range(self.col):
                if random.randint(1,9)!=5:
                    self.mat[i][j]=random.randint(1,aval)
    
    def addcol(self,lst:list):
        '''Добавляет столбец в конец матрицы со значениями из lst '''
        if lst==[] or len(lst)==self.row:
            self.col+=1
            for i in range(self.row):
                if lst==[]:
                    self.mat[i].append(None)
                else:
                    self.mat[i].append(lst[i])
            
    
    def addrow(self,lst:list):
        '''Добавляет строку в конец матрицы со значениями из lst '''
        if lst==[] or len(lst)==self.col:
            self.row+=1
            if lst==[]:
                self.mat.append([None for i in range(self.col)])
            else:
                self.mat.append(lst)
    
    def get_val(self,arow: int,acol:int):

        ''' Возвращает значение ячейки матрицы на позицию arow, acol
         исчисление начинается с 1
        '''
        if (1<=acol<=self.col) and (1<=arow<=self.row):
            return self.mat[arow-1][acol-1]
        else: print('get_val: Out of range')
    
    def set_val(self,arow:int,acol:int,aval):
        ''' Записывает значение aval в матрицу на позицию acol, arow
         исчисление начинается с 1
        '''
        if (1<=acol<=self.col) and (1<=arow<=self.row):
            self.mat[arow-1][acol-1]=aval
        else: print('set_val: Out of range')

    def get_dimension(self):
        ''' Возвращает кортежем кол-во столбцов и строк в матрице'''
        return self.col,self.row
        
    
    

                        
                    


    
matr=Matrix(5,5)
matr.randomval(100)
print(matr)
print('get=',matr.get_val(5,5)) 
print('get=',matr.get_val(3,3)) 
matr.set_val(5,5,555)
matr.set_val(3,3,333)
print(matr)
print('Размер матрицы:',matr.get_dimension())
matr.addcol(['1','2','3','4','5'])
print(matr)
print('Размер матрицы:',matr.get_dimension())
matr.addrow([1,2,3,4,5,6])
print(matr)
print('Размер матрицы:',matr.get_dimension())

mat1=Matrix(4,4)
mat2=Matrix(4,4)
mat1.randomval(10)
mat2.randomval(10)
# for i in range(1,5):
#     for j in range(1,5):
#         mat1.set_val(i,j,i)
#         mat2.set_val(i,j,i)
print(mat1)
print(mat2)
print("mat1==mat2:", mat1==mat2)
mat3=mat1+mat2
print('Сложение матриц')
print(mat3)
