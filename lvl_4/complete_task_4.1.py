# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def get_connection():
    con=sqlite3.connect('./lvl_4/teatchers.db')
    return con
def close_connection(con):
    if con:
        con.close()

def create_tbl(tblname,tblstruct):
    try:
        con=get_connection()
        curs=con.cursor()
        sqlstr='CREATE TABLE IF NOT EXISTS '+tblname+' '+tblstruct 
        curs.execute(sqlstr)
        close_connection(con)
    except (Exception,sqlite3.Error) as err:
        print(f'Что-то пошло не так! Ошибка: {err}')

def add_data(tblname,adata):
    try:
        con=get_connection()
        curs=con.cursor()
        sqlstr='INSERT INTO '+tblname+' VALUES (?,?,?);' 
        curs.execute(sqlstr,(adata))
        con.commit()
        close_connection(con)
    except (Exception,sqlite3.Error) as err:
        print(f'Что-то пошло не так! Ошибка: {err}')

def add_data_many(tblname,adata):
    try:
        con=get_connection()
        curs=con.cursor()
        sqlstr='INSERT INTO '+tblname+' VALUES (?,?,?);' 
        curs.executemany(sqlstr,adata)
        con.commit()
        close_connection(con)
    except (Exception,sqlite3.Error) as err:
        print(f'Что-то пошло не так! Ошибка: {err}')

tblname='Student'

#*****Создание таблицы Student****
stud_struct='''(Student_Id INTEGER NOT NULL, Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL PRIMARY KEY);'''
#create_tbl(tblname,stud_struct)

# *****Добавление данных в таблицу*****
stud_data=[(201, 'Иван', 1), (202, 'Петр', 2), (203, 'Анастасия', 3), (204, 'Игорь', 4)]
# for st in stud_data:
#     add_data(tblname,st)

#add_data_many(tblname,stud_data)

# ****Вывод данных по студенту***
def get_student_info(stud_id):
    try:
        con=get_connection()
        curs=con.cursor()
        # sqlstr='''SELECT * FROM School JOIN Student ON School.School_Id=Student.School_Id 
        # WHERE Student.Student_Id = ?;'''
        sqlstr='''SELECT * FROM Student JOIN School ON Student.School_Id=School.School_Id 
        WHERE Student.Student_Id = ?;'''
        curs.execute(sqlstr,(stud_id,))
        stud_list=curs.fetchall()
        if stud_list==[]:
            print(f'Студент с ID: {stud_id} не найден\n')
        else:
            for st in stud_list:
                print(f'ID студента: {st[0]}')
                print(f'Имя студента: {st[1]}')
                print(f'ID школы: {st[3]}')
                print(f'Наименование школы: {st[4]}\n')
        
        close_connection(con)
    except (Exception,sqlite3.Error) as err:
        print(f'Что-то пошло не так! Ошибка: {err}')

get_student_info(201)
get_student_info(202)
get_student_info(206)