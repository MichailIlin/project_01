# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    ss=''
    for ch in s:
        if ch!='!':
            ss+=ch
    return ss


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    ch=s[-1:]
    if ch=="!":
        return s[0:len(s)-1]
    else: return s


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    rs=''
    ls=s.split(' ')
    if len(ls)>0:
        for i in ls:
            
            if i.count('!')!=1:
                rs+=i+' '
    return rs.rstrip()
    




print('*'*10,'Func remove_exclamation_marks','*'*10)
src='Source string! Original String!!!'
print("before:",src)
rs=remove_exclamation_marks(src)
print("after:",rs)

src='!!!'
print("before:",src)
rs=remove_exclamation_marks(src)
print("after:",rs)
print()

print('*'*10,'Func remove_last_em','*'*10)
src='!!!test !! abc!!!'
print("before:",src)
rs=remove_last_em(src)
print("after:",rs)
print()

print('*'*10,'Func remove_word_with_one_em','*'*10)
src="Hi! !Hi! Hi!"
print("before:",src)
rs=remove_word_with_one_em(src)
print("after:",rs)
