# INPUT   =>   is identical to prompt() in JS
# RU:  идентичен prompt() в JS
# -----------------------------------
# GETTING STRING PARTS (==> '---'.slice())
# '...'[start:end:step] [начало:конец:шаг]
# 'Hello'[0:2]    # He
# 'Hello'[0:5:2]  # Hlo
# 'Hello'[::2]    # Hlo
# 'Hello'[::-1]   # olleH

# -----------------------------------
# INCLUDES
# print(" " in "Hello world")
# "..." in "..."  => checks if the other string is
#                    included in the string

# -----------------------------------
# REPLACE
# .replace('...', '...')  (==> .replaceAll())
# print("Hello world".replace('o', "*"))

# import re  # Regular Expressions

# x = "I love an Apple but sometimes I eat an orange or BANANA"
# y = ["apple", "orange", "banana"]  # "apple|orange|banana"
# # [..., ..., ...].join("|")  is in JS
# y = "|".join(y)
# --------------------------------------
# print("BEFORE:  => ", x)
# x = re.sub(
#     "|".join(y),
#     "***",
#     x,
#     flags=re.IGNORECASE
# )
# print("AFTER:  => ", x)
# --------------------------------------
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


# capitalize()      Converts the first character to upper case
#               RU: преобразует первый символ в верхний регистр
# print("hello world".capitalize())  # Hello world
# ===================================
# title()          Converts the first character of each word to upper case
#               RU: преобразует первый символ каждого слова в верхний регистр
# print("hello world".title())  # Hello World
# ===================================
# istitle()          Returns True if the string follows the rules of a title
#               RU: Возвращает True, если строка соответствует правилам заголовка
# print("Hello World".istitle())  # False
# ===================================
# upper()          Converts a string into upper case
#               RU: преобразует строку в верхний регистр
# print("hello world".upper())  # HELLO WORLD
# ===================================
# lower()          Converts a string into lower case
#               RU: преобразует строку в нижний регистр
# print("HELLO WORLD".lower())  # hello world
# ===================================
# casefold()      Converts string into lower case
#               RU: преобразует строку в нижний регистр
# print('Hello WORLD'.casefold())  # hello world
# The main difference is casefold() is stronger than lower() method,
# it converts more characters into lower case
# RU: Основное отличие в том, что метод casefold() сильнее, чем метод lower(),
# он преобразует больше символов в нижний регистр
# ===================================
# isupper()          Returns True if all characters in the string are upper case
#               RU: Возвращает True, если все символы в строке в верхнем регистре
# print("HELLO WORLD".isupper())  # True
# ===================================
# islower()          Returns True if all characters in the string are lower case
#               RU: Возвращает True, если все символы в строке в нижнем регистре
# print("HELLO WORLD".islower())  # False
# ===================================
# center()          Returns a centered string
#               RU: Возвращает центрированную строку
# print("Testing center".center(30, "*"))  # False
# ********Testing center********
# ===================================
# count()          Returns the number of times a specified value occurs in a string
#               RU: Возвращает количество раз, когда в строке встречается указанное значение
# print("Test text for checking the count() method".count("t"))  # 6
# print("Test text for checking the count() method".count("text"))  # 1
# ===================================
# endswith()      Returns true if the string ends with the specified value
#               RU: Возвращает true, если строка заканчивается указанным значением
# print("Test text".endswith("text"))  # True
# print("Test text".endswith("www"))   # False
# ===================================
# startswith()      Returns true if the string starts with the specified value
#               RU: Возвращает true, если строка начинается с указанного значения
# print("Test text".startswith("Test"))  # True
# print("Test text".startswith("www"))   # False
# ===================================
# expandtabs()      Sets the tab size of the string  (EX:  "H\te\tl\tl\to" ==>  "H    e    l    l    o")
#               RU: Устанавливает размер табуляции строки
# test_text = "H\tello w\torl\td"
# print(test_text.expandtabs(1))  # H ello w orl d
# print(test_text.expandtabs(5))  # H    ello w     orl  d
# ===================================
# find()          Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking the find() method"
# print(test_text.find("test"))  # 8
# print(test_text.find("www"))   # -1
# ===================================
# rfind()          Searches the string for a specified value and returns the last position of where it was found  (==> .lastIndexOf()
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.rfind("test"))  # 31
# print(test_text.rfind("www"))  # -1
# ===================================
# index()          Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.index("www"))  # raises ValueError
# ===================================
# rindex()          Searches the string for a specified value and returns the
#                   last position of where it was found (==> lastIndexOf in JS)
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# ===================================
# swapcase()      Swaps cases, lower case becomes upper case and vice versa
#               RU: Меняет регистр, нижний регистр становится верхним и наоборот
# test_text = "HeLLo world"
# print(test_text.swapcase())  # hEllO WORLD
# ===================================
# format()          Formats specified values in a string
#               RU: Форматирует указанные значения в строке
# x = "Updated"
# z1 = "Test text for {var} checking .format()".format(var=x)
# z2 = f"Test text for {x} checking .format()"
# print(z1)
# print(z2)
# ===================================
# isalnum()          Returns True if all characters in the string are alphanumeric
#               RU: Возвращает True, если все символы в строке являются буквенно-цифровыми
# x = "Hello777"
# print(x.isalnum())  # True
# ===================================
# isalpha()       Returns True if all characters in the string are in the alphabet
#               RU: Возвращает True, если все символы в строке находятся в алфавите
# x = "Hello"
# print(x.isalpha()) # True
# x = 777
# print(x.isalpha()) # False
# ===================================
# isdecimal()      Returns True if all characters in the string are decimals
# ==             RU: Возвращает True, если все символы в строке являются десятичными
# isdigit()       Returns True if all characters in the string are digits
# ==             RU: Возвращает True, если все символы в строке являются цифрами
# isnumeric()      Returns True if all characters in the string are numeric
#               RU: Возвращает True, если все символы в строке являются числовыми
# x = "123"
# print(x.isnumeric())  # True
# print(x.isdigit())    # True
# print(x.isdecimal())  # True
# ===================================
# isspace()          Returns True if all characters in the string are whitespaces
#               RU: Возвращает True, если все символы в строке являются пробелами
# x = "   "
# print(x.isspace())  # True
# ===================================
# join()          Joins the elements of an iterable to the end of the string
#               RU: Объединяет элементы итерируемого объекта в конец строки
# x = ["Text 1", "Text 2", "Text 3"]
# print("|".join(x))  # Text 1|Text 2|Text 3
# print("".join(x))   # Text 1Text 2Text 3
# print(" ".join(x))   # Text 1 Text 2 Text 3
# ===================================
# ljust()          Returns a left justified version of the string  (==> padStart in JS)
#               RU: Возвращает левую версию строки
# rjust()          Returns a right justified version of the string (==> padEnd in JS)
#               RU: Возвращает правую версию строки
# test_txt = "Hello"
# print(test_txt.ljust(20, "*"))
# print(test_txt.rjust(20, "*"))
# ===================================
# strip()          Returns a trimmed version of the string         (==> trim in JS)
#              RU: Возвращает усеченную версию строки
# x = "   Hello world   "
# print(x.strip())  # "Hello world"
# ===================================
# replace()          Returns a string where a specified value is replaced with a specified value
#              RU: Возвращает строку, в которой указанное значение заменяется на указанное значение
# ===================================
# split()          Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список
# x = "Text 1, Text 2, Text 3"
# print(x.split(","))  # ['Text 1', ' Text 2', ' Text 3']

# If we want to split by letters, we can use list()
# x = list(x)
# print(x)
# ===================================
# rsplit(maxsplit)Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список
# x = "Text 1, Text 2, Text 3"
# x = x.rsplit(" ")
# print(x)
# print(x) # ["Text 1, Text 2", " Text 3"]

# x.rsplit(" ", 2)  => ['Text 1, Text 2,', 'Text', '3']
# x.rsplit(" ")  => ['Text', '1,', 'Text', '2,', 'Text', '3']
# ===================================
# list()           For splitting string-letters into list
#              RU: Для разделения букв строки на списке
#   EX: list('Hello') ==> ['H', 'e', 'l', 'l', 'o']
# x = "Text 1, Text 2, Text 3"
# print(list(x))
# ===================================
# splitlines()     Splits the string at line breaks and returns a list
#              RU: Разделяет строку по переводам строк и возвращает список
# x = "This is \n test \n text"
# print(x)
# print(x.splitlines())
# ===================================
# zfill()          Fills the string with a specified number of 0 values at the beginning
#              RU: Заполняет строку указанным количеством значений 0 в начале
# x = "Hello"
# print(x.zfill(10))  # 00000Hello
