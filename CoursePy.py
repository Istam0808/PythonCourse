#Istam Company

# _________  _______  _________  ________
#     |      |            |      |      |    |\          /|         
#     |      |            |      |      |    | \        / |           
#     |      |_____       |      |______|    |  \      /  |     _____        
#     |            |      |      |      |    |   |    |   |     __\\_  COMPANY     
#     |            |      |      |      |    |    \  /    |       
# ____|____   _____|      |     /        \  /      \/      \     
                                                            


lesson = 'Introduction'
"""
# IN Python
# ------------
# String   ("...", '...')
# triple "   =>   Multiline comment
# '''...'''   =>   Multiple comment
# "..."   =>   String (text)
# '...'   =>   String (text)

# String(123) => "123"  => in JS
# str(123)    => "123"  => in Python
# ----------------------------------------
# int()   =>   parseInt()
# type()  =>   typeof()
# ----------------------------------------
# print(int(123.5))
# print(float("123"))

# print(type("123"))      # <class 'str'>
# print(type(int("123")))  # <class 'int'>
# print(type(float("123")))  # <class 'float'>
# ----------------------------------------
# `${...}`  => String template   => JS
# f'...'   =>  Formatted string  => Python
# ----------------------------------------
# print("This is", test,  end="!!!", sep="---")
# ----------------------------------------
# test = 'Hello world'       # Global variable
# test = "Updated text"      # Update global variable
# ----------------------------------------
# x = [1, 2, 3]
# a = x[0]
# b = x[1]
# c = x[2]
# a, b, c = x
# print(a, b, c, sep="-")
# ----------------------------------------
# x = [1, 2, 3, 4, 5, 6, '...']
# first, *others, last = x
# print(first)
# print(others)
# print(last)
# ----------------------------------------
# function ...() {}
# def ...():   #  =>  def == define
# ____...

# def test():
#     global x, y
#     x = 10
#     y = 20
#     print("Hello world")  # this is inside function

# test()                # This line calls function
# print("Hello world")  # this line is out of function
# print(x)              # This line calls global variable
# -------------------------------------------------------
# x = 10
# print(x)
# del x
# print(x)

# let x = {
#     name: 'John',
# }
# delete x['name']
# -------------------------------------------------------
# input   =>  allows us to get input from user
# answer = input("How are you? ")
# print("You typed: " + answer)
# -------------------------------------------------------
# if ...:
#     ...
# elif ...:
#     ...
# else:
#     ...

"""


lesson = 'numbers'
"""
# math.ceil    => 3.33 => 4
# math.floor() => 3.33 => 3
# round()      => 3.5  => 4   => is used to round the number by 
#                               deleting the decimal part if it is 
#                               less than 5
#                       2nd param => number of digits after the decimal point
#                       RU: используется для округления числа путем 
#                           удаления десятичной части, если она меньше 5
#                       2-й параметр => количество цифр после десятичной точки
# ----------------------------------------------------------------------
# import random
# ----------------------------------------------------------------------
# random.randrange(.., ..?) # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex:  random.randrange(0, 10, step=2)  # 0, 2, 4, 6, 8
# ----------------------------------------------------------------------
# random.randint(.., ..)   # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex: random.randint(0, 10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# ----------------------------------------------------------------------
# random.random()    # gives random float number between 0 and 1
#            RU: дает случайное число с плавающей запятой между 0 и 1
# ex: round(random.random() * 100, 5)
# ----------------------------------------------------------------------

# int()       # 1
# float()     # 1.0
# complex()   # 1j

# ----------------------------------------------------------------------

# FIND PERCENTAGE
# (60 / 100) * 17  # 10.2
# 60 * 0.17        # 10.2

# ----------------------------------------------------------------------

# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	   
# %	    Modulus	        x % y	   =>    10 % 3  =>  1
# **	Exponentiation	x ** y	   =>    2 * 2 * 2 * 2   =   2**4   => 16
#! //	Floor division	x // y     =>    x // 2   => 3.5 => 3
#! -------------------------------------------------

# =	    x = 5	 x = 5	  
# +=	x += 3	 x = x + 3	
# -=	x -= 3	 x = x - 3	
# *=	x *= 3	 x = x * 3	
# /=	x /= 3	 x = x / 3	
# %=	x %= 3	 x = x % 3	
# **=	x **= 3	 x = x ** 3	
#! //=	 x //= 3	 x = x // 3	

# ----------------------------------------------------------------------

# ==	Equal	        x == y	  =>  Равно
# !=	Not equal	    x != y	  =>  Не равно
# >	    Greater than	x > y	  =>  Больше
# <	    Less than	    x < y	  =>  Меньше
# >=	Greater than or equal to	x >= y	  =>  Больше или равно
# <=	Less than or equal to	    x <= y    =>  Меньше или равно

# ----------------------------------------------------------------------

# and 	Returns True if both statements are true	    x < 5 and  x < 10	
#     RU: Возвращает True, если оба выражения истинны
# or	Returns True if one of the statements is true	x < 5 or x < 4	
#     RU: Возвращает True, если одно из выражений истинно
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10
#     RU: Инвертирует результат, возвращает False, если результат истинен

# ----------------------------------------------------------------------

# is 	    Returns True if both variables are the same object	
#       RU: Возвращает True, если обе переменные являются одним и тем же объектом
# ex:   x is y	

# is not	Returns True if both variables are not the same object	
# ex:   x is not y
#       RU: Возвращает True, если обе переменные не являются одним и тем же объектом

# ----------------------------------------------------------------------

# in 	    Returns True if a sequence with the specified value is 
#           present in the object	
#       RU: Возвращает True, если последовательность с указанным значением
#           присутствует в объекте
# ex:    x in y
	
# not in	Returns True if a sequence with the specified value is 
#           not present in the object
#       RU: Возвращает True, если последовательность с указанным значением
#           отсутствует в объекте
# ex:    x not in y


# ----------------------------------------------------------------------
#!     *args  => is used receive an arbitrary number of arguments
#  RU: используется для получения произвольного количества аргументов

# def sum(*args) -> int:
#         # This function returns sum of two numbers
#         # RU: Эта функция возвращает сумму двух чисел
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(sum(1, 2, 3, 4, 5))
# ----------------------------------------------------------------------
"""


lesson = 'if/elif/else  &&  match/case  &&  Exercises'
"""
# Bool   =>   bool()
# ------------------------------------------------------------------
# If / elif / else 
# if 1==2:
#     print(f'1 == 1 is => {1==2}')
# elif 1==1:
#     print(f'1 == 1 is => {1==1}')
# else:
#     print(1==2)
# ------------------------------------------------------------------
# match / case
# HTTPS_status = 200
# match HTTPS_status:
#     case 200 | 201:
#         print('OK')
#     case 404:
#         print('Not found')
#     case 301 | 302:
#         print('Redirect')
#     case _:
#         print('Unknown')
# ------------------------------------------------------------------

# EXERCISES
# 1. Reverse and input from a user    &&    Reverse a number
# RU: 
#     Берите текст от клиента и выведите на терминале. 
#     Найти зеркальное число.
# inp = input("What is your name: ")
# print(inp[::-1])
# print(str(num)[::-1])
# ----------------------------------------------------------
# 2. Swap first and last digits of a number
# RU: Поменяйте местами первую и последнюю цифры числа.
# x = 123456789
# x = str(x)
# print(int(x[-1] + x[1:-1] + x[0]))
# ----------------------------------------------------------
# 3. check if a string is a palindrome

def is_polindrome(arg) -> bool:
    if type(arg) == int:
        arg = str(arg)
    # if isinstance(arg, int):
    #     arg = str(arg)
    return arg == arg[::-1]
print(is_polindrome(input('Guess a polindrome: ')))
# ----------------------------------------------------------

# SOLUTIONS FOR PREVIOUS EXERCISES
# print(str(num)[::-1])
# print(input('Enter a number: ')[::-1])
# print(str(num)[-1] + str(num)[1:-1] + str(num)[0])
# print(str(num) == str(num)[::-1])
"""


lesson = 'strings'
"""
# INPUT   =>   is identical to prompt() in JS
# RU:  идентичен prompt() в JS
# -----------------------------------
# GETTING STRING PARTS (==> .slice())
# '...'[start:end:step] [начало:конец:шаг]
# 'Hello'[0:2]  # He
# 'Hello'[0:5:2]  # Hlo
# 'Hello'[::2]  # Hlo
# 'Hello'[::-1] # olleH
# -----------------------------------
# INCLUDES
# len('Hello')  # 5
# "..." in "..."  => checks if the other string is 
#                    included in the string

# -----------------------------------
# REPLACE
# .replace('...', '...')  (==> .replaceAll())
# import re  # Regular Expressions
# x = "I love an Apple but sometimes I eat an orange or BANANA"
# y = ["apple", "orange", "banana"] # "apple|orange|banana"
# # [..., ..., ...].join("|")  is in JS
# y = "|".join(y)
# print("BEFORE:  => ", x)
# x = re.sub(
#     "apple|orange|banana",
#     "***",
#     x,
#     flags=re.IGNORECASE
# )
# print("AFTER:  => ", x)

# re.sub(
#     #   '...'   or    r'[^a-z]'   or    '...|...|...',  
#     #   replacement,
#     #   original_string
#     #   flags=re.IGNORECASE
# ) 
# EXAMPLES:
    # text = "Mentioning of reD, GrEen and BLUE is prohibited"
    # words_to_replace = ["red", "green", "blue"]
    # new_text = re.sub(f'{"|".join(words_to_replace)}',
    #                 "***",
    #                 text,
    #                 flags=re.IGNORECASE)
    # print(new_text)
# ----------------------------------------------------------------------------------
# MODIFYING STRINGS


# capitalize()	    Converts the first character to upper case
#               RU: преобразует первый символ в верхний регистр
# print("hello world".capitalize())  # Hello world
# ===================================
# title()	        Converts the first character of each word to upper case
#               RU: преобразует первый символ каждого слова в верхний регистр
# print("hello world".title()) # Hello World
# ===================================
# istitle()	        Returns True if the string follows the rules of a title
#               RU: Возвращает True, если строка соответствует правилам заголовка
# print("hello world".istitle())  # False
# ===================================
# upper()	        Converts a string into upper case
#               RU: преобразует строку в верхний регистр
# print("hello world".upper())  # HELLO WORLD
# ===================================
# lower()	        Converts a string into lower case
#               RU: преобразует строку в нижний регистр
# print("HELLO WORLD".lower())  # hello world
# ===================================
# casefold()	    Converts string into lower case
#               RU: преобразует строку в нижний регистр
# print('Hello WORLD'.casefold())  # hello world
# The main difference is casefold() is stronger than lower() method, 
# it converts more characters into lower case
# RU: Основное отличие в том, что метод casefold() сильнее, чем метод lower(),
# он преобразует больше символов в нижний регистр
# ===================================
# isupper()	        Returns True if all characters in the string are upper case
#               RU: Возвращает True, если все символы в строке в верхнем регистре
# print("HELLO WORLD".isupper())  # True
# ===================================
# islower()	        Returns True if all characters in the string are lower case
#               RU: Возвращает True, если все символы в строке в нижнем регистре
# print("HELLO WORLD".islower())  # False
# ===================================
# center()	        Returns a centered string
#               RU: Возвращает центрированную строку
# print("Testing center".center(30, "*"))  # False
# ********Testing center********
# ===================================
# count()	        Returns the number of times a specified value occurs in a string
#               RU: Возвращает количество раз, когда в строке встречается указанное значение
# print("Test text for checking the count() method".count("t")) # 6
# print("Test text for checking the count() method".count("text")) # 1
# ===================================
# endswith()	    Returns true if the string ends with the specified value
#               RU: Возвращает true, если строка заканчивается указанным значением
# print("Test text".endswith("text"))  # True
# print("Test text".endswith("www"))   # False
# ===================================
# startswith()	    Returns true if the string starts with the specified value
#               RU: Возвращает true, если строка начинается с указанного значения
# print("Test text".startswith("Test"))  # True
# print("Test text".startswith("www"))   # False
# ===================================
# expandtabs()	    Sets the tab size of the string  (EX:  "H\te\tl\tl\to" ==>  "H    e    l    l    o")
#               RU: Устанавливает размер табуляции строки 
# test_text = "H\tello w\torl\td"
# print(test_text.expandtabs(1))  # H ello w orl d
# print(test_text.expandtabs(5))  # H    ello w     orl  d
# ===================================
# find()	        Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking the find() method"
# print(test_text.find("test"))  # 8
# print(test_text.find("www"))   # -1
# ===================================
# rfind()	        Searches the string for a specified value and returns the last position of where it was found  (==> .lastIndexOf()
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.rfind("test")) # 31
# print(test_text.rfind("www"))  # -1
# ===================================
# index()	        Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.index("www")) # raises ValueError 
# ===================================
# rindex()	        Searches the string for a specified value and returns the 
#                   last position of where it was found (==> lastIndexOf in JS)
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# ===================================
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
#               RU: Меняет регистр, нижний регистр становится верхним и наоборот
# test_text = "HeLLo world"
# print(test_text.swapcase())  # hEllO WORLD
# ===================================
# format()	        Formats specified values in a string
#               RU: Форматирует указанные значения в строке
# x = "Updated"
# z = "Test text for {var} checking .format()".format(var=x)
# z = f"Test text for {x} checking .format()"
# print(z)
# ===================================
# isalnum()	        Returns True if all characters in the string are alphanumeric
#               RU: Возвращает True, если все символы в строке являются буквенно-цифровыми
# x = "Hello777"
# print(x.isalnum()) # True
# ===================================
# isalpha() 	    Returns True if all characters in the string are in the alphabet
#               RU: Возвращает True, если все символы в строке находятся в алфавите
# x = "Hello"
# print(x.isalpha()) # True
# x = 777
# print(x.isalpha()) # False
# ===================================
# isdecimal()	    Returns True if all characters in the string are decimals
#==             RU: Возвращает True, если все символы в строке являются десятичными
# isdigit() 	    Returns True if all characters in the string are digits
#==             RU: Возвращает True, если все символы в строке являются цифрами
# isnumeric()	    Returns True if all characters in the string are numeric
#               RU: Возвращает True, если все символы в строке являются числовыми
# x = "123"
# print(x.isdecimal())  # True
# print(x.isdigit())    # True
# print(x.isnumeric())  # True
# ===================================
# isspace()	        Returns True if all characters in the string are whitespaces
#               RU: Возвращает True, если все символы в строке являются пробелами
# x = "   "
# print(x.isspace())  # True
# ===================================
# join()	        Joins the elements of an iterable to the end of the string
#               RU: Объединяет элементы итерируемого объекта в конец строки
# x = ["Text 1", "Text 2", "Text 3"]
# print("|".join(x))  # Text 1|Text 2|Text 3
# print("".join(x))   # Text 1Text 2Text 3
# print(" ".join(x))   # Text 1 Text 2 Text 3

# ===================================
# ljust()	        Returns a left justified version of the string  (==> padStart in JS)
#               RU: Возвращает левую версию строки
# rjust()	        Returns a right justified version of the string (==> padEnd in JS)
#               RU: Возвращает правую версию строки
# test_txt = "Hello"
# print(test_txt.ljust(20, "*"))
# print(test_txt.rjust(20, "*"))
# ===================================
# strip()	        Returns a trimmed version of the string         (==> trim in JS)
#              RU: Возвращает усеченную версию строки
# x = "   Hello world   "
# print(x.strip()) # "Hello world"
# ===================================
# replace()	        Returns a string where a specified value is replaced with a specified value 
#              RU: Возвращает строку, в которой указанное значение заменяется на указанное значение
# ===================================
# split()	        Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список
# x = "Text 1, Text 2, Text 3"
# print(x.split(",")) # ['Text 1', ' Text 2', ' Text 3']
# ===================================
# rsplit(maxsplit)Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список  
# x = "Text 1, Text 2, Text 3"
# x = x.rsplit(",", 1)
# print(x) # ["Text 1, Text 2", " Text 3"]
# ===================================
# list()           For splitting string-letters into list
#              RU: Для разделения букв строки на списке
#   EX: list('Hello') ==> ['H', 'e', 'l', 'l', 'o']
# x = "Text 1, Text 2, Text 3"
# print(list(x))
# ===================================
# splitlines()	   Splits the string at line breaks and returns a list
#              RU: Разделяет строку по переводам строк и возвращает список
# x = "This is \n test \n text"
# print(x)
# print(x.splitlines())
# ===================================
# zfill()	        Fills the string with a specified number of 0 values at the beginning
#              RU: Заполняет строку указанным количеством значений 0 в начале
# x = "Hello"
# print(x.zfill(10)) # 00000Hello
# ===================================
# 'Hello'[::-1]    Reverses a string
#              RU: Переворачивает строку

"""


lesson = 'try-except  &  Exceptions  &  Generators'
"""
# number types  => int, float, complex
# str
# sequence =>  list, tuple, range
# searching type, mapping   =>  dict  (Object in JS)
# set  =>   set, frozenset
# binary type  =>  bytes, bytearray, memoryview
# bool  => True, False
# None  => None
# =========================================================================
# 0 = 0
# 1 = 1
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# ...
# =========================================================================
# In JavaScript
# try {}  catch {}  =>  попробуй, если получится, а если нет то перехвати ошибку
# =========================================================================
# In Python
# try: ...   except: ...  => попробуй, если получится, а если нет то пропускай ошибку
# =========================================================================
# from typing import Union
# try:
#     x = 'Hello world'
#     print(x).print(x)
# except Union[NameError, TypeError]:
#     print('Переменная не объявлена')
# =========================================================================
# Types of errors
# 1. SyntaxError  =>  не правильно написан код и 
#                      невозможно его прочитать для питона
# EX:  1. print("Hello world)
#      2. print("Hello world'))
# ------------------------
# 2. TypeError    =>  не правильно написан код и
#                      питон не может выполнить действие
# EX:  1. print(5 + 'Hello world') 
#      2. print(5 + [1, 2, 3])
# ------------------------
# 3. NameError    =>  не правильно написан код и
#                     питон не может найти переменную
# EX:  1. print(x)
#      2. print(y)

# =========================================================================
# 2==2 ? True : False  => In JavaScript
# -------------------------------------
# Ternary operator in Python
# "Yes" if condition==True else "No"
# if 2==2:
#     print('Yes')
# else:
#     print('No')
# # ------------------------
# print("yes") if 2==2 else "No"
# =========================================================================
# Range
# range(10)  =>  range(0, 10)
# list(range(10))  => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(10, 20))  => [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# list(range(10, 30, 5))  => [10, 15, 20, 25]
# =========================================================================
# for num in range(10, 50, 2):
#     print(num) if num%10==0 else print('Not devidible to 10')
# =========================================================================

# ERROR TYPES
1. SyntaxError  =>  '...  => not closed string
    - Forgetting to put a closing quote on a string.
    - Forgetting to put a colon at the end of a def, while, for, or if statement.

2. TypeError    =>  1 + '...'  =>  unsupported operand type(s) for +: 'int' and 'str'
    - Trying to add a string to an integer or float.
    - Trying to add a list or tuple to an integer or float.

3. NameError    =>  x  =>  name 'x' is not defined
    - Trying to use a variable that does not exist.
    - Trying to use a function or method that does not exist.

4. IndexError   =>  [1, 2, 3][3]  =>  list index out of range
    - Trying to access an index in a list that does not exist.

5. ValueError   =>  int('...')  =>  invalid literal for int() with base 10: '...'
    - Converting a string to an integer or float, but the string is not a valid number.
    - Converting a string to a boolean, but the string is not 'True' or 'False'.
    - Using the datetime.datetime.strptime() function with a string that does not match the specified format string.
    - Using the json.loads() function with a string that is not valid JSON.

6. KeyError     =>  {'a': 1}['b']  =>  'b' =>  not in dictionary
    - Trying to access a key in a dictionary that does not exist.

7. AttributeError  =>  'Hello'.append('!')  =>  'str' object has no attribute 'append'
    - Trying to use a method on a data type that does not have that method.
    - Trying to access an attribute that does not exist.
    
8. ZeroDivisionError  =>  1 / 0  =>  division by zero
    - Trying to divide a number by zero.
    
9. ImportError  =>  import math  =>  No module named 'math'
    - Trying to import a module that does not exist.
    
10. IndentationError  =>  def func():  =>  expected an indented block
    - Forgetting to indent the code inside a function, while, for, or if statement.
    
# ============================================================================
# =============================================================================
# Generators
# Using a for loop to generate a list of even numbers up to 10^6
import time
def even_nums():
    for i in range(1000000):
        if i % 2 == 0:
            yield i
    # result = []
    # for i in range(1000000):
    #     if i % 2 == 0:
    #         result.append(i)
    # return result


# Using a generator to generate a list of even numbers up to 10^6
before = time.time()
even_nums_gen = even_nums()
after = time.time()
print(list(even_nums_gen))
print(round(after - before, 5))
# =========================================================================
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fibonacci()
for i in range(10):
    print(next(g))  # Output: 0 1 1 2 3 5 8 13 21 34
# =========================================================================
"""


lesson = 'functions  &&  lambda  &&  Exercises'
"""
# def func_name(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
# func_name(1, 2, 3)
# ----------------------------------------------------------
# from typing import Union
# def func_name(arg1:Union[str, int]) -> type:
#     return arg1
# print(func_name(1))
# ----------------------------------------------------------
# default value
# ----------------------------------------------------------
# Lambda
# func_name = lambda arg1, arg2: arg1 + arg2
# print(func_name(1, 2))
# ----------------------------------------------------------
# def show_message(*children):
#     # This function needs to be finished in near future!
#     # return NotImplementedError()  =>  не было создано!
#     pass
# """


lesson = "Range && List"
"""
# range(10)              => range(0, 10)
# list(range(10))        => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10, 20)    #     => range(10, 20)
# range(10, 20, 2) #     => range(10, 20, 2)
# list(range(10, 20, 2)) => [10, 12, 14, 16, 18]
# ---------------------------------------------------------
# for (let i=0; i<10; i++) {}
# for num in range(10):
#     print(num)
#     # num = num + 1
#     num += 1
# typeof([])        =>  object
# print(type([]))   =>  <class 'list'>
# ---------------------------------------------------------
# UPDATE
# x_list[...:...] = [...]   =>  updates from ... to ... by [...]
# ---------------------------------------------------------
# ADD
# [].insert(position, element_to_add) => вставлять
# [].append()  =>  добавит элемент в конец листа
# [].extend()  =>  добавит элементы в конец листа
# ---------------------------------------------------------
# REMOVE
# "..." in x  =>  проверяет есть ли элемент в листе
# [].pop()     =>  удаляет последний элемент
# [].remove()  =>  удаляет элемент по значению
# ---------------------------------------------------------
# COPY
# [].copy() => копирует лист
# ---------------------------------------------------------
# SORT
# [].sort(reverse=True)  => меняет оригинальный лист
# sorted([])             => не меняет оригинальный лист 
#                  и можно присвоить новой переменной
# ---------------------------------------------------------
# REVERSE
# [].reverse() =>  меняет оригинальный лист
"""


lesson = "Tuples"
"""
############################ List comprehension
[ <expression> for x in <sequence> if <condition> ]
##-----------------------------------------------------
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)
# ---------------------------------------------
users = ['Aziz', 'Jomol', "Farzod", "Diana", "Laziz"]

# [x…() for … in … if … ]

z = [ name for name in users if name.endswith('z') ]
for name in users:
    if name.endswith('z'):
        z.append(name)
        
# ---------------------------------------------

# [if … else for … in … ]
a = [ name if name.endswith('z') else 'Not Found' for name in users ]
for name in users:
    if name.endswith('z'):
        a.append(name)
    else:
        a.append('Not Found')

# ---------------------------------------------
        
arr = range(100)
s = [f"Even {num}" if num%2==0 else f"Odd {num}" for num in list(arr) if num<50]
# for num in list(arr):
#     if num%2==0:
#         s.append(f"Even {num}")
#     else:
#         s.append(f"Odd {num}")
# print(s)
# ---------------------------------------------
# def double(arr):
#     return [num*2 for num in arr]
# print(double([1,2,3,4,5,6,7,8,9,10]))
# ---------------------------------------------


############################ TUPLE
# []  =>  mutable           =>  Можно изменять
# ()  =>  immutable         =>  Нельзя изменять
# ---------------------------------------------
# Tuple comprehension
# x = tuple([fruit.title() for fruit in x])
# for item in x:
#     print(item.upper())
# ---------------------------------------------
# ordered      =>  means that every item has its own index starting from 0 
#              RU: каждый элемент имеет свой индекс, начиная с 0
# unchangeable =>  means that we can not change the items after the tuple 
#                  has been created
#              RU: после создания кортежа мы не можем изменить его элементы
# Tuple Length  =>  len()

########### Двоичная система
# 0 = 0
# 1 = 1
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# 10 = 1010
# 11 = 1011
# 12 = 1100
# 13 = 1101
# 14 = 1110
# 15 = 1111
# 16 = 10000


########### Fibonacci
# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
# We have to add the last two numbers to get the next number
# RU: Мы должны добавить последние два числа, чтобы получить следующее число
# --------------------------------------------------------------------------

# Create Tuple With One Item   =>   ('...',)
# tuple()                      =>   tuple([..., ...])
# Change Tuple Values          =>   x = list(("apple", "banana", "cherry")) 

# Unpacing 
# let [x,y] = [1, 2]

# Using Asterisk*   ||    _ * _   ||   _ _ *
# a, *b, c = ("apple", "banana", "cherry")

# Multiply 
# print(("apple", "banana", "cherry") * 2)

# -------------------------------------------------------------------
# append()	Adds an element at the end of the list
# RU:      Добавляет элемент в конец списка
# clear()	Removes all the elements from the list
# RU:      Удаляет все элементы из списка
# copy()	Returns a copy of the list
# RU:      Возвращает копию списка
# count()	Returns the number of elements with the specified value
# RU:      Возвращает количество элементов с указанным значением
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# RU:      Добавляет элементы списка (или любого итерируемого объекта) в конец текущего списка
# index()	Returns the index of the first element with the specified value
# RU:      Возвращает индекс первого элемента с указанным значением
# insert()	Adds an element at the specified position
# RU:      Добавляет элемент в указанную позицию
# pop()	    Removes the element at the specified position
# RU:      Удаляет элемент в указанной позиции
# remove()	Removes the item with the specified value
# RU:      Удаляет элемент с указанным значением
# reverse()	Reverses the order of the list
# RU:      Изменяет порядок списка на обратный
# sort()	Sorts the list (changes the original)          [].sort()
# RU:      Сортирует список (изменяет оригинал)
# sorted()	Sorts the list (does not change the original)  sorted([])
# RU:      Сортирует список (не изменяет оригинал)
"""


lesson = "Dictionaries  =>  словарь"
"""
# x = {"first": "Один", "second": "Два",
#     "third": "Три", "fourth": "Четыре",
#     "fifth": "Пять", "sixth": "Шесть",
#     "seventh": "Семь", "eighth": "Восемь",
# }
# print(x.get("fourth", "Не нашлось"))
# ------------------------------------------------
# z = [ "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь" ]
# for i in z:
#     if i == "Четыре":
#         print(i)
# ------------------------------------------------

# dict()  =>  dict(key=value, key=value, key=value)

# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}



# # ACCESSING ITEMS ---------------------------------------------------------------------------

# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default
# dict.keys()       => возвращает список ключей
# dict.values()     => возвращает список значений
# dict.items()      => возвращает список кортежей (ключ, значение)

# # ADDING ITEMS -----------------------------------------------------------------------------
# dict[key] = value
# -----------------
# dict.update({key:value, key:value, key:value})
# person.update({"name": "Alex", "address": "Samarkand"})
# -----------------
# dict.setdefault(key, value)
# person.setdefault("address", "Tashkent")


# # REMOVING ITEMS ---------------------------------------------------------------------------

# dict.pop(key)
# dict.pop(key, default)
# dict.popitem() => removes the last inserted item
# del dict[key]
# del dict

# # MERGE ------------------------------------------------------------------------------------
# dict1.update(dict2)
# dict1 |= dict2
# dict1 |= dict2 | dict3 | dict4
# {**dict1, **dict2, **dict3, **dict4}

# person2 = { "name2":"John",  "age2":20,  "surname2":"Khan",  "address2":"Samarkand" }
# person3 = {1:'a', 2:'b'}
# -----------------------------------
# person |= person2 | person3 
# -----------------------------------
# a = {**person, **person2, **person3 } 
# works like spread operator in JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# dict.clear()
# dict.copy()

# for key in person.keys():
#     person[key] = ""

# p2 = person.copy()
# p2.update({"name":"Ali"})
# print(p2)
# print(person)

# person = {
#     "name": "John",
#     "age": 20,
#     "surname": "Khan",
#     "address": "Samarkand"
# }

# dict.fromkeys(iterable, value)  -> is used to create a new dictionary from the given 
#                                    sequence of elements with a value provided by the user.
# EX: 
# x = dict.fromkeys(['name', 'age'], 'unknown')
# print(x)

# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# from random import randint
# def random_dict_of_github_issue_ids(stop: int, max_count: int, start: int = 0):
#     return dict.fromkeys(
#         [str(randint(start, stop)) for _ in range(randint(0, max_count))], ""
#     )
# print(random_dict_of_github_issue_ids(100, 10))
# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# zip() function
# zip(iterator1, iterator2, ...)
# Result: ...(zip object)  =>  (1, 'a'), (2, 'b'), (3, 'c')

# itr1 = list('abcdefghijklmnopqrstuvwxyz')
# itr2 = range(len(itr1))
# zipped = zip(itr1, itr2)

# for (item, item2) in zipped:
#     print(item, item2)

# # --------------------------------------------------------------------------------------------
# # DICTIONARY COMPREHENSIONs-------------------------------------------------------------------

# # Using range() function and no input list
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)


# # Lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# # Using one input list
# numdict = {x:x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# # Using two input lists
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)
"""


lesson = "Sets"
"""
# my_set = {"apple", "banana", "cherry"}
# print(my_set)

# # or use the set function and create from an iterable, e.g. list, tuple, string
# my_set_2 = set(["one", "two", "three"])
# my_set_2 = set(("one", "two", "three"))
# print(my_set_2)

# my_set_3 = set("aaabbbcccdddeeeeeffff")
# print(my_set_3)

# # careful: an empty set cannot be created with {}, as this is interpreted as dict
# # use set() instead
# a = {}
# print(type(a))
# a = set()
# print(type(a))
# # {'banana', 'apple', 'cherry'}
# # {'three', 'one', 'two'}
# # {'b', 'c', 'd', 'e', 'f', 'a'}
# # <class 'dict'>
# # <class 'set'>


# # -----------------------------------------------------------------------------------
# # NOTES  -----------------------------------------------------

# test_set = {1, 2, 3, 4, 5}
# # Don't allow duplications
# # Doesn't have order, index, keys, values, items, slices, etc...


# # 1 and True are the same and 0 and False are the same
# # 1 == True  =>  True
# # 0 == False  =>  True
# # 1 is True  =>  False
# # 0 is False  =>  False


# # -----------------------------------------------------------------------------------
# # ACCESSING ITEMS --------------------------------------------
# # loop   ||    ... in ...


# # -----------------------------------------------------------------------------------
# # ADDING -----------------------------------------------------

# # add()	                Adds an element to the set
# #   EX: x.add(4)  => changes the original set

# # update()	            Updates the set with the union of this set and others
# #  EX: x.update([4, 5, 6])  => changes the original set


# # -----------------------------------------------------------------------------------
# # Union and Intersection

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# # union() : combine elements from both sets, no duplication
# # note that this does not change the two sets
# u = odds.union(evens)
# print(u)
# # EX:
# # a = x.union(y)  # =>  x | y

# # intersection(): take elements that are in both sets
# # return a new set, that only contains the items that are present in both sets.
# i = odds.intersection(evens)  # =>  x & y
# print("intersection 1: ", i)  # =>  {}
# # EX: x.intersection(y) #  =>  x & y

# i = odds.intersection(primes)  # => {3, 5, 7}
# print("intersection 2: ", i)

# i = evens.intersection(primes)  # => {2}
# print("intersection 3: ", i)


# # -----------------------------------------------------------------------------------
# # DIFFERENCE of sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3,                   10, 11, 12}

# # difference() : returns a set with all the elements from the setA that are not in setB or in C,D... .
# # x.difference(y)     =>  x - y
# # x.difference(y, z)  =>  x - y - z

# diff_set = setA.difference(setB)
# print("difference 1: ", diff_set)

# # A.difference(B) is not the same as B.difference(A)
# diff_set = setB.difference(setA)
# print("difference 2: ", diff_set)

# # symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
# diff_set = setA.symmetric_difference(setB)
# print("difference 3: ", diff_set)

# # A.symmetric_difference(B) = B.symmetric_difference(A)
# diff_set = setB.symmetric_difference(setA)
# print("difference 4: ", diff_set)


# # -----------------------------------------------------------------------------------
# # DELETE

# # remove(x): removes x, raises a KeyError if element is not present
# my_set = {"apple", "banana", "cherry"}
# my_set.remove("apple")
# print(my_set)

# # KeyError:
# # my_set.remove("orange")

# # discard(x): removes x, does nothing if element is not present
# my_set.discard("cherry")
# my_set.discard("blueberry")
# print(my_set)

# # clear() : remove all elements
# my_set.clear()
# print(my_set)

# # pop() : return and remove a random element
# a = {True, 2, False, "hi", "hello"}
# print(a.pop())
# print(a)

# # -----------------------------------------------------------------------------------
# # Check if element is in Set
# my_set = {"apple", "banana", "cherry"}
# if "apple" in my_set:
#     print("yes")


# # -----------------------------------------------------------------------------------
# # UPDATE sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3,                    10, 11, 12}

# # update() : Update the set by adding elements from another set.
# setA.update(setB)
# print("Set update", setA)

# # Keep ONLY the Duplicates
# # intersection_update() : Update the set by keeping only the elements found in both
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.intersection_update(setB)
# print("Set intersection_update", setA)

# # difference_update() : Update the set by removing elements found in another set.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.difference_update(setB)
# print("Set difference_update", setA)

# # symmetric_difference_update():  Keeps only the elements that are NOT present in both sets.
# # Keep All, But NOT the Duplicates.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.symmetric_difference_update(setB)
# print("Set symmetric_difference_update", setA)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])

# # -----------------------------------------------------------------------------------
# # Copying ---------------------------------------------------------------------------
# set_org = {1, 2, 3, 4, 5}

# # this just copies the reference to the set, so be careful
# set_copy = set_org

# # now modifying the copy also affects the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)

# # use copy() to actually copy the set
# set_org = {1, 2, 3, 4, 5}
# set_copy = set_org.copy()

# # now modifying the copy does not affect the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)


# # -----------------------------------------------------------------------------------
# # Subset, Superset, and Disjoint ----------------------------------------------------
# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# # issubset(setX): Returns True if setX contains the set
# print(setA.issubset(setB))
# print(setB.issubset(setA))  # True

# # issuperset(setX): Returns True if the set contains setX
# print(setA.issuperset(setB))  # True
# print(setB.issuperset(setA))

# # isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
# setC = {7, 8, 9}
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))
# # -----------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # FROZENSET
# # Frozen set is just an immutable version of normal set.
# # While elements of a set can be modified at any time, elements of frozen set
# # remains the same after creation. Creation with: my_frozenset = frozenset(iterable)

# a = frozenset([0, 1, 2, 3, 4])

# # The following is not allowed:
# # a.add(5)
# # a.remove(1)
# # a.discard(1)
# # a.clear()

# # Also no update methods are allowed:
# # a.update([1,2,3])

# # Other set operations work
# odds = frozenset({1, 3, 5, 7, 9})
# evens = frozenset({0, 2, 4, 6, 8})
# print(odds.union(evens))
# print(odds.intersection(evens))
# print(odds.difference(evens))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# frozenset()
# frozenset({1, 3, 5, 7, 9})

"""


lesson = "LOOPS"
"""
# ----------WHILE LOOP
# SYNTAXIS
# while condition == True:
#   do something
# ----------FOR LOOP
# SYNTAXIS
# for x in []:
#   print(x)
# ----------ENUMERATE
# enumerate is used to get an index for the item that we are taking from list
# ex:
#   for index, item in enumerate(list):
#       print(index, item)

# ==============================================================================
# break     => breaks up the current loop
# RU: прерывает текущий цикл
# continue  => skips the current iteration of the loop
# RU: пропускает текущую итерацию цикла
# ---------
# fruits = ["apple", "banana", "kiwi", "disgusting cherry", "mango"]
# for fruit in fruits:
#     if 'disgusting' in fruit:
#         break
#     elif 'kiwi' == fruit:
#         continue
#     else:
#         print(fruit)
# ==================================================================
# round((time.time() - start_time), 2)
# ------------
# round   => rounds the number to the specified number of digits
# RU: округляет число до указанного количества цифр
# EX: print(round(3.454, 2)) => 3.45
# ------------
# import time
# time.time() => returns the number of seconds passed since epoch
# EX: start_time = time.time()
#     end_time = time.time()
#     difference = end_time - start_time
# 
# from datetime import datetime as dt
# start_time = dt.now()
# for n in range(100):
#     print(n)
#     for n2 in range(100):
#         print(n2)

# end_time = dt.now()
# print("Execution time: ", end_time - start_time)
# ==================================================================
# import random
# letters = "abcdefghijklmnopqrstuvwxyz"
# letters_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# numbers = "1234567890"
# symbols = "@#$%^&*"

# total_symbols_for_password = 20
# everything_included = letters + numbers + symbols

# created_password = ""
# for i in range(total_symbols_for_password):
#     random_int = random.randint(0, len(everything_included)-1)
#     created_password += everything_included[random_int]

# print(created_password)
# ==================================================================
"""


lesson = "File handling"
"""
# CREATE A FILE
# To create non-existing file we use "x" mode
# Also, if the file IS FOUND then it returns an error
# ex: 
# f = open("myfile.txt", "x") # =>  x mode allows to create a 
                                # file if it does not exist, 
                                # otherwise it raises an error.
# if we don't want to get an error then we have to use os
# import os
# if os.path.exists("myfile.txt"):
#   print("The file exists")
# ===========================================================
# READ FILE
# When we open the file we have to always remember to close it
# If we don't close it then we can't open it again until we restart the program
# For reading the file we use 'r' mode
# Also, if the file is NOT FOUND then it returns an error

# 1. read()      => reads whole file (we also can specify how many characters to read)
# 2. readline    => reads only one line
# 3. readlines() => reads the file line by line (all lines)
# 4. loop through the file line by line

# ex:
#   f = open("myfile.txt", "r")
#       print(f.read())

# ===========================================================
# UPDATE A FILE
# To update an existing file, we use "a" mode or "w" mode
# --- (w)  write mode replaces the content of the file
# --- (a)  append mode appends the content to the end of the file
# ex:  
#   f = open("myfile.txt", "a")
#   f.write("Now the file has more content!")
#   ----------------------------
#   using keyword WITH
#   with open("myfile.txt", "a") as f:
#       f.write("Now the file has more content!")
# ===========================================================
# DELETE A FILE
# To delete a file, we use os.remove() function
# ex:
#   import os
#   os.remove("myfile.txt")

# ===========================================================
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Combinations of modes:
"a+" - Read and Append - Opens a file for reading and appending, creates the file if it does not exist
"w+" - Write and Read - Opens a file for writing and reading, creates the file if it does not exist
"r+" - Read and Write - Opens a file for reading and writing, error if the file does not exist

# ===========================================================
# WORKING WITH DIRECTORIES and os
# import os
# os.mkdir("myfolder") # => creates a folder
# os.rmdir("myfolder") # => removes a folder
# os.rename("oldname", "newname") # => renames a folder
# os.getcwd() # => returns the current working directory
# os.path.exists("myfolder") # => checks if the folder exists
# os.path.isdir("myfolder") # => checks if the folder exists
# os.path.isfile("myfile.txt") # => checks if the file exists
# os.path.join("myfolder", "myfile.txt") # => joins the folder and the file
"""


lesson = "Class  &&  OOP"
_1 = 'Abstract and Inheritance'
"""
# Abstract
# Inheritance

# this == self

# class User:
#     def __init__(self, name):
#         print(f"User {name} is created")
#         self.name = name

# user1 = User("John")
# print(user1)
# print(user1.name)


# __init__  => is a constructor method which is used to initialize the attributes of a class
# it is called automatically when an object is created

#############################################################################################
################ Abstraction

# "abc" here stands for abstract base class. It is first imported and then used as 
# a parent class for some class that becomes an abstract class. Its simplest implementation 
# can be done as below.


# from abc import ABC, abstractmethod
# class AbcAnimal(ABC):
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food

#     @abstractmethod
#     def get_description(self):
#         pass
#         # raise NotImplementedError


# class Pets(AbcAnimal):
#     def __init__(self, name, food, speed):
#         super().__init__(name, food)
#         self.speed = speed

#     def get_description(self):
#         return f"{self.name} eats {self.food}"


# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_description())



# abs module is used to create abstract classes
# it is helpful when we want to create a class that will be used as a base class
# abstractmethod is used to declare abstract methods which will be implemented by the child classes
# is it used to ensure that the child classes will have the same method as the parent class
# and returns an error if the child class does not have the same method as the parent class
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.

#############################################################################################
################ Inheritence

# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def test(self):
#         print("Hello world")

# class Child(Parent, ABC):
# #     Inherited members from parent class
# #     Additional members of the child class
#     def __init__(self, name, age):
#         super().__init__(name)  # => calls the parent class constructor
#         self.age = age

#     def test(self):
#         print("Hello world from child")

#     def __repr__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for debugging and logging.
#         '''
#         return f"{self.name} is {self.age} years old"

#     def __str__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for the end user.
#         '''
#         return f"{self.name} is {self.age} years old"


# child = Child("John", 20)
# print(child)
# print(child.test())
"""

_2 = 'Polymorphism and Encapsulation and Decorators'
"""
################ Polymorphism
# Polymorphism allows you define one interface and have multiple implementations.
# Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return self.name+' says Woof!'
#
# class Cat(Animal):
#     def speak(self):
#         return self.name+' says Meow!'


#############################################################################################
################ Encapsulation
# is used to restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.

# class Alpha:
    # def __init__(self):
    #     self._a = 2.  # Protected member ‘a’
    #     self.__b = 2.  # Private member ‘b’




#############################################################################################
#################### DECORATORS

# @property   is a built-in decorator in Python that is used to define the properties
#             of an object. The @property decorator makes the work easier by
#             automatically calling the getter method when the value of the attribute is accessed.

# @classmethod is a built-in decorator in Python that is used to create class methods.
#              The class method can be called by both the class and the object.
#              This method accepts the class as the first argument that is passed automatically
#              when the method is called.

# @staticmethod is a built-in decorator in Python that defines a static method.
#               A static method doesn’t receive any reference argument whether it is called by an
#               instance of a class or by the class itself. This means that a static method can neither
#               modify object state nor class state. Static methods are restricted in what data they can
#               access - and they’re primarily a way to namespace your methods.

# -- Static method knows nothing about the class and just deals with the parameters.
# -- Class method works with the class since its parameter is always the class itself.

# Link that is about difference of two decorators:
# https://sparkbyexamples.com/python/python-difference-between-staticmethod-and-classmethod/#h-1-what-is-staticmethod


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     @staticmethod
#     def isAdult(age):
#         return age > 18

# student1 = Student('Rolf', 19)
# student2 = Student.fromBirthYear('Anna', 1990)

# print(student1.age)
# print(student2.age)


####################################################################################
####################################################################################
_3 = 'Dunder methods'

from abc import ABC, abstractmethod


class AbstractUserClass(ABC):
    name: str
    surname: str
    age: int
    email: str

    @abstractmethod
    def get_info(self):
        raise NotImplementedError(
            "This is an abstract method and needs to be implemented in the child class.")


class User(AbstractUserClass):
    def __init__(self, name: str, surname: str, age: int = 0, email: str = '') -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def __str__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'

    def __call__(self, *args, **kwargs):
        print(f"This is call fn from __call__")
        for i in args:
            print(i)
        return ''
        # ex:
        # user1("test1", "test2", "test3")  => This is call fn from __call__

    def __add__(self, other):
        return "This user has $" + str(other.budget)

    def get_info(self):
        print(f'{self.name} {self.surname}')
        return ''

    @classmethod
    def from_string(cls, string):
        if not string.count(',') == 3:
            raise Exception("String must have 4 values separated by comma.")

        # string  =>  "John, Doe, 25, test@gmail.com"
        splitted_str = string.split(",")
        name, surname, age, email = splitted_str
        # name = splitted_str[0]
        # surname = splitted_str[1]
        # age = splitted_str[2]
        # email = splitted_str[3]
        return cls(name, surname, int(age), email)

    @staticmethod
    def is_adult(age):
        return age > 18


class Client(User):
    def __init__(self, name: str, surname: str, budget: float) -> None:
        super().__init__(name, surname)
        self.budget = budget

    def __str__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def get_info(self):
        print(f'{self.name} {self.surname} has ${self.budget} budget.')
        return ''


# # =================================================
# user1 = User('John', 'Doe', 25, 'test@gmail.com')
# print(user1.get_info())
# # =================================================
# client1 = Client("Cathrine", "Mackwold", 10000)
# print(client1.get_info())
# # =================================================
# result = user1 + client1
# print(result)
# =================================================
# user1 = User.from_string("John, Doe, 25, test@gmail.com")  # classmethod
# print(user1)
# print(User.is_adult(user1.age))  # staticmethod
"""

# EXERCISES
# https://pynative.com/python-object-oriented-programming-oop-exercise/