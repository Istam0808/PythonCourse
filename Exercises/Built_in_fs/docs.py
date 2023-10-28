# 1. max()
# Return the largest item in an iterable or the largest of two or more arguments.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.

# If one item is given, it should be iterable. The largest item in the iterable is returned.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.
# max(iterable, *[, key, default])

# If two or more positional arguments are provided, the largest of the positional arguments is returned.
# RU: Если предоставлено два или более позиционных аргумента, возвращается наибольший из позиционных аргументов.
# max(arg1, arg2, *args[, key])

# There are two optional keyword-only arguments.
# RU: Есть два необязательных аргумента только ключевых слов.

# key- key function where the iterables are passed and comparison is performed based on its return value
# RU: key- ключевая функция, в которой передаются итерируемые объекты,
# и сравнение выполняется на основе возвращаемого значения
# EX:
#   iterable = ['geeks', 'code', 'python', 'java']
#   max(iterable, key=len)  =>  'python'
# iterable = [30, 15, 20, 25, 30]
# print(max(iterable, key=lambda x: x%15))  # => 25
#   => here the remainder after dividing each element by
#      15 is calculated and the maximum of those values is returned
#      ex:  10%15 = 10,  15%15 = 0,  20%15 = 5,  25%15 = 10,  30%15 = 0

# The default argument specifies an object to return if the provided iterable is empty.
# If the iterable is empty and the default is not provided, a ValueErroris raised.
# EX:
#   iterable = []
#   max(iterable, default=100)  =>  100
#   max(iterable)  =>  ValueError: max() arg is an empty sequence
# ==================================
# 2. min()         Works the same way as max(), but returns the smallest value


# ===========================================================================================
# 3. map()         Returns a map object (which is an iterator) of the results after applying the
#               given function to each item of a given iterable (list, tuple etc.)
#           RU: Возвращает объект отображения (который является итератором) результатов после применения
#               заданной функции к каждому элементу заданного итерируемого объекта (список, кортеж и т. Д.)
#           EX:
#               def wordCount(n):
#                   return len(n)
#               x = map(wordCount, ('apple', 'banana', 'cherry'))
#               print(list(x))  => [5, 6, 6]
# ------------------------------------------------------------------------------
# 4. filter()      Use a filter function to exclude items in an iterable object
#           RU: Используйте функцию фильтра, чтобы исключить элементы в итерируемом объекте
#           EX:
#               def myFunc(n):
#                   # if n > 18:
#                   #     return True
#                   # else:
#                   #     return False
#                   -------------------
#                   # return True if n > 18 else False
#                   -------------------
#                   return n > 18

#               x = filter(myFunc, (5, 7, 18, 25, 32))
#               print(list(x))  =>  [25, 32]
# ------------------------------------------------------------------------------
# 5. reduce()      Use a function to reduce an iterable to a single value
#           RU: Используйте функцию для сокращения итерируемого объекта до одного значения
#           EX:
# from functools import reduce
# def myFunc(acc, next):
#     """
#         acc  - accumulator
#         next - next value
#         NOTE: the initial value of the accumulator is the first value of the iterable
#               if not given as last argument
#     """
#     return acc + next
#     # return acc if acc > next else next

# x = reduce(myFunc, (1, 2, 3, 4))
# print(x)  # =>  10

# ------------------------------------------------------------------------------
# 6. abs()	        Returns the absolute value of a number
#           RU: Возвращает абсолютное значение числа
#           EX:
#               x = -2   ==   abs(x) == 2
#               z = 2    ==   abs(z) == 2
#               c = complex(2)
#               print(c)
#               x = abs(c)
#               print(x)
# ------------------------------------------------------------------------------
# 7. all()	        Returns True if all items in an iterable object are true
#           RU: Возвращает True, если все элементы в итерируемом объекте истинны
#           EX:

# all()  ==  and  ==  &&
# any()  ==  or   ==  ||

# mylist = [True, True, False]
# x = all(mylist)  # =>  True
# print(x)
# ------------------------------------------------------------------------------
# 8. any()	        Returns True if any item in an iterable object is true
#           RU: Возвращает True, если любой элемент в итерируемом объекте истинен
#           EX:
# mylist = [False, False, True]
# x = any(mylist)  # => True
# print(x)
# ------------------------------------------------------------------------------
# 9. ascii()	    Returns a readable version of an object. Replaces none-ascii characters with escape character
#       American Standard Code for Information Interchange
#           RU: Возвращает читаемую версию объекта. Заменяет символы, не являющиеся ASCII-символами, символом экранирования
#           EX:
# x = ascii("My name is Ståle")  # => 'My name is St\xe5le'

# ------------------------------------------------------------------------------
"""
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
"""
# 10. bin()	        Returns the binary version of a number
#           RU: Возвращает двоичную версию числа
#           EX:
#               x = bin(36)  =>  0b100100
# vice versa is =>  int(0b100100)  =>  36

# ------------------------------------------------------------------------------
# 11. bool()	    Returns the boolean value of the specified object
#               Anything that is not empty, or 0, or None is True
#           RU: Возвращает логическое значение указанного объекта
#               Любое значение, которое не является пустым, или 0, или None, является True
#           EX:

#               x = bool(5) => True,     x = bool(0) => False,   ...
# ------------------------------------------------------------------------------
# 12. bytes()   Returns a bytes object
#           RU: Возвращает объект байтов
#           EX:
#               x = bytes(5)  =>  b'\x00\x00\x00\x00\x00'
# ------------------------------------------------------------------------------
# 13. callable()	Returns True if the specified object is callable, otherwise False
#          RU: Возвращает True, если указанный объект может быть вызван, иначе False
#          EX:
# def x():
#     return 5
# z = 0
# print(callable(x))  # =>  True
# print(callable(z))  # =>  False
# ------------------------------------------------------------------------------
# Unicode codes:  They are used to represent text in computer and other devices,
#                 such as phones and tablets. You can also use them in HTML.
#                 More info: https://www.w3schools.com/charsets/ref_html_ascii.asp
#   0 - 31	    Control codes
#   32 - 126	Printable characters
#   127	        Delete
#   128 - 159	Extended codes
#   160 - 255	International characters

# 14. chr()	        Returns a character from the specified Unicode code.
#          RU: Возвращает символ из указанного кода Unicode.
#          EX:
# x = chr(97)  # =>  a
# print(x)

# ------------------------------------------------------------------------------
# 15. classmethod()	Converts a method into a class method
#         RU: Преобразует метод в метод класса
#         EX:
#               class Person:
#                   age = 25
#                   def printAge(cls):
#                       print('The age is:', cls.age)
#               Person.printAge = classmethod(Person.printAge)
#               Person.printAge()  =>  The age is: 25
# ------------------------------------------------------------------------------
# 16. complex()	    Returns a complex number (x+yj) or converts a string or number to a complex number
#           RU: Возвращает комплексное число (x + yj) или преобразует строку или число в комплексное число
#           EX:
#               x = complex(3, 5)  =>  (3+5j)
# ------------------------------------------------------------------------------
# 17. delattr()	    Deletes the specified attribute (property or method) from the specified object
#           RU: Удаляет указанный атрибут (свойство или метод) из указанного объекта
#           EX:
# person = {
#     'name': 'John',
#     'age': 36,
#     'country': 'Norway'
# }
# delattr(person, 'age')
# del person['age']
# ------------------------------------------------------------------------------
# 18. dict()	    Returns a dictionary (Array)
#           RU: Возвращает словарь (массив)
#           EX:
# x = dict(name = 'John', age = 36, country = 'Norway')
# ------------------------------------------------------------------------------
# 19. dir()	        Returns a list of the specified object's properties and methods
#           RU: Возвращает список свойств и методов указанного объекта
#           EX:
# x = dir(bool)

# [print(z) for z in x]
# ------------------------------------------------------------------------------
# 20. enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
#           RU: Принимает коллекцию (например, кортеж) и возвращает ее в виде объекта перечисления
#           EX:
# x = ['apple', 'banana', 'cherry']
# y = enumerate(x)
# print(list(y))  # =>  [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# for (index, value) in enumerate(x):
#     print(f'{index} => {value}')

# ------------------------------------------------------------------------------
# 21. float()	    Returns a floating point number
# print(float(2)) # => 2.0
# ------------------------------------------------------------------------------

# 22. frozenset()	Returns a frozenset object
# ------------------------------------------------------------------------------
# 23. getattr()	    Returns the value of the specified attribute (property or method)
#           RU: Возвращает значение указанного атрибута (свойства или метода)
#           EX:
# class Person:
#     name = 'John'
#     age = 36
#     country = 'Norway'
# NOTE: does not work with dictionaries
# x = getattr(Person, 'age')
# print(x)
# ------------------------------------------------------------------------------
# 24. globals()	    Returns the current global symbol table as a dictionary
#           RU: Возвращает текущую глобальную таблицу символов в виде словаря
# ex:
#   x = 10
#   y = 5
#   globals = globals()  =>  []
#   print(globals['x'])  =>  10
# ------------------------------------------------------------------------------
# 25. hasattr()	 dictmethod    Returns True if the specified object has the specified attribute (property/method)
#           RU: Возвращает True, если указанный объект имеет указанный атрибут (свойство / метод)
#           EX:
# class Person:
#     name = 'John'
#     age = 36
#     country = 'Norway'
# x = hasattr(Person, 'age')
# print(x)
# ------------------------------------------------------------------------------
# 26. hash()	    Returns the hash value of a specified object
#           RU: Возвращает хеш-значение указанного объекта
#           EX:
#               x = hash('Hello')
#               print(x)  =>  8317319708700421212
# -------------------
# The hash value is used to uniquely identify a specific object
# The get the value from the hash object we can use special id for saving the hashed
# version of the object
# By using id we can get the value from the hash object back from DB

# -------------------
# Когда мы хотим сохранить объект в базу данных, мы можем использовать хеш-значение
# Если мы хотим получить значение из объекта хеша, мы можем использовать
# специальный идентификатор для сохранения хешированной версии объекта
# Используя идентификатор, мы можем получить значение из объекта хеша
# обратно из базы данных

# ------------------------------------------------------------------------------
# 27. help()	    Executes the built-in help system
#           RU: Выполняет встроенную систему справки
#           EX:
#               print(help('modules'))
#               print(help('print'))
#               ...

# ------------------------------------------------------------------------------
# 28. hex()	        Converts a number into a hexadecimal value
#           RU: Преобразует число в шестнадцатеричное значение
#           EX:
# x = hex()  # =>  0xff
# ------------------------------------------------------------------------------
# 29. id()	        Returns the id of an object
#           RU: Возвращает идентификатор объекта
#           EX:
# x = ('apple', 'banana', 'cherry')
# print(id(x))  # =>  140714640543488
# print(id(list))

# ------------------------------------------------------------------------------
# 30. input()	    Allowing user input
# ------------------------------------------------------------------------------
# 31. int()	        Returns an integer number
# ------------------------------------------------------------------------------
# 32. isinstance()	Returns True if a specified object is an instance of a specified object
#           RU: Возвращает True, если указанный объект является экземпляром указанного объекта
#           EX:
#               x = isinstance(5, int)
# ------------------------------------------------------------------------------
# 33. issubclass()	Returns True if a specified class is a subclass of a specified object
#           RU: Возвращает True, если указанный класс является подклассом указанного объекта
#           EX:
#               class Person:
#                   name = 'John'
#                   age = 36
#
#               class Student(Person):
#                   grade = 9
#
#               x = issubclass(Student, Person)
# ------------------------------------------------------------------------------
# 34. iter()	    Returns an iterator object
#           RU: Возвращает объект итератора
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
#               print(next(x))  =>  cherry
#               print(next(x))  =>  StopIteration
# ------------------------------------------------------------------------------
# 35. len()	        Returns the length of an object
# ------------------------------------------------------------------------------
# 36. list()	    Returns a list
# ------------------------------------------------------------------------------
# 37. next()	    Returns the next item in an iterable
#           RU: Возвращает следующий элемент в итерируемом объекте
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
# ------------------------------------------------------------------------------
# 38. oct()	        Converts a number into an octal
#           RU: Преобразует число в восьмеричное число
#           EX:
#               x = oct(8)  =>  0o10
# ------------------------------------------------------------------------------
# 39. open()	    Opens a file and returns a file object
# ------------------------------------------------------------------------------
# 40. ord() 	    Convert an integer representing the Unicode of the specified character
#           RU: Преобразовать целое число, представляющее Юникод указанного символа
#           EX:
#               x = ord('h')  =>  104
# ------------------------------------------------------------------------------
# 41. pow()	        Returns the value of x to the power of y
# pow(3, 4) # 81   ==>   3 ** 4    ==>   3 * 3 * 3 * 3

# ------------------------------------------------------------------------------
# 42. print()	    Prints to the standard output device
# ------------------------------------------------------------------------------
# 42. property	Gets, sets, deletes a property
#           RU: Получает, устанавливает, удаляет свойство
#           EX:
#               class Person:
#                   def __init__(self, name, age):
#                       self.name = name
#                       self.age = age
#
#                   @property
#                   def fullName(self):
#                       return self.name + ' ' + self.age
# ------------------------------------------------------------------------------
# 44. range()	    Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# ------------------------------------------------------------------------------
# 45. repr()	    Returns a readable version of an object
#           RU: Возвращает читаемую версию объекта
#           More info:
#           https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/repr/python-repr/#:~:text=a%20Python%20repr%3F-,The%20Python%20repr()%20method%20is%20mostly%20used%20for%20the,specified%20object%20as%20a%20string.
#
#           EX:
#               x = repr('Hello')
#               print(x)  =>  'Hello'
# ------------------------------------------------------------------------------
# 46. reversed()	Returns a reversed iterator
#           RU: Возвращает обратный итератор
#           EX:
#               x = reversed(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  cherry
# ------------------------------------------------------------------------------
# 47. round()	    Rounds a numbers
#           RU: Округляет числа
#           EX:
#               x = round(5.76543, 2)
#               print(x)  =>  5.77
# ------------------------------------------------------------------------------
# 48. set()	        Returns a new set object
# ------------------------------------------------------------------------------
# 49. setattr()	    Sets an attribute (property/method) of an object
#           RU: Устанавливает атрибут (свойство / метод) объекта
#           EX:
#               class Person:
#                   name = 'John'
#                   age = 36
#               x = setattr(Person, 'age', 40)
# ------------------------------------------------------------------------------
# 50. slice()	    Returns a slice object
#           RU: Возвращает объект среза
#           EX:
#               x = slice(3)
#               fruits = ['apple', 'banana', 'cherry', 'orange']
#               print(fruits[x])  =>  ['apple', 'banana', 'cherry']
# ------------------------------------------------------------------------------
# 51. sorted()	    Returns a sorted list
#           RU: Возвращает отсортированный список
#           EX:
#               x = sorted(['apple', 'banana', 'cherry', 'orange'])
# ------------------------------------------------------------------------------
# 52. staticmethod()	Converts a method into a static method
# ------------------------------------------------------------------------------
# 53. str()	        Returns a string object
# ------------------------------------------------------------------------------
# 54. sum()	        Sums the items of an iterator
# ------------------------------------------------------------------------------
# 55. super()	    Returns an object that represents the parent class
# ------------------------------------------------------------------------------
# 56. tuple()	    Returns a tuple
# ------------------------------------------------------------------------------
# 57. type()	    Returns the type of an object
# ------------------------------------------------------------------------------
# 58. vars()	    Returns the __dict__ property of an object
#           RU: Возвращает свойство __dict__ объекта
#           EX:
#               class Person:
#                   name = 'John'
#                   age = 36

#               x = vars(Person)
#               print(x)  =>  {'name': 'John', 'age': 36}
# ------------------------------------------------------------------------------
# 59. zip()	        Returns an iterator, from two or more iterators
#           RU: Возвращает итератор из двух или более итераторов
#           EX:
#               x = zip(['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple'])
#               print(next(x))  =>  ('apple', 'orange')
# fruits = ['apple', 'banana', 'cherry', 'orange', 'lemon', 'pineapple']
# cars = ['BMW', 'Volvo', 'Ford', 'Mazda']
# z = zip(fruits, cars)
# for (fruit, car) in z:
#     print(fruit, car)

# x = [1, 2, 3, 4, 5]
# z = ['a', 'b', 'c']

# for num, letter in zip(x, z):
#     print(num, letter)

# ------------------------------------------------------------------------------
# 60. format()	    Formats a specified value
# my_name = 'Alisher'
# my_age = 28
# z = "Hello, my name is {name} and my age is {age}".format(name=my_name, age=my_age)
# print(z)


#! for more info visit sites:
# * 1. Programmiz  =  https://www.programiz.com/python-programming/methods/built-in
# * 2. w3schools   =  https://www.w3schools.com/python/python_ref_functions.asp
# * 3. python.org  =  https://docs.python.org/3/library/functions.html
