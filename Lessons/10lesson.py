# ------------------------------------------------------------------------------
# 6. abs()          Returns the absolute value of a number
#           RU: Возвращает абсолютное значение числа
#           EX:
#               x = -2   ==   abs(x) == 2
#               z = 2    ==   abs(z) == 2
#               c = complex(2)
#               print(c)
#               x = abs(c)
#               print(x)
# ------------------------------------------------------------------------------
# 7. all()          Returns True if all items in an iterable object are true
#           RU: Возвращает True, если все элементы в итерируемом объекте истинны
#           EX:

# all()  ==  and  ==  &&
# any()  ==  or   ==  ||

# mylist = [True, True, False]
# x = all(mylist)  # =>  False
# print(x)
# ------------------------------------------------------------------------------
# 8. any()          Returns True if any item in an iterable object is true
#           RU: Возвращает True, если любой элемент в итерируемом объекте истинен
#           EX:
# mylist = [False, False, True]
# x = any(mylist)  # => True
# print(x)
# ------------------------------------------------------------------------------
# 9. ascii()      Returns a readable version of an object. Replaces none-ascii characters with escape character
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
# 10. bin()          Returns the binary version of a number
#           RU: Возвращает двоичную версию числа
#           EX:
#               x = bin(36)  =>  0b100100
# vice versa is =>  int(0b100100)  =>  36

# ------------------------------------------------------------------------------
# 11. bool()      Returns the boolean value of the specified object
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
# 13. callable()  Returns True if the specified object is callable, otherwise False
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
#   0 - 31      Control codes
#   32 - 126  Printable characters
#   127          Delete
#   128 - 159  Extended codes
#   160 - 255  International characters

# 14. chr()          Returns a character from the specified Unicode code.
#          RU: Возвращает символ из указанного кода Unicode.
#          EX:
# x = chr(223)  # =>  ß
# print(x)
# with the help of <<alt+number>> we can get the unicode code
# RU: с помощью <<alt + number>> мы можем получить код Unicode

# ------------------------------------------------------------------------------
# 15. classmethod()  Converts a method into a class method
#         RU: Преобразует метод в метод класса
#         EX:
# class Person:
#     age = 25
#     @classmethod
#     def printAge(cls):
#         print('The age is:', cls.age)
# # Person.printAge = classmethod(Person.printAge)
# Person.printAge() #=>  The age is: 25
# ------------------------------------------------------------------------------
# 16. complex()      Returns a complex number (x+yj) or converts a string or number to a complex number
#           RU: Возвращает комплексное число (x + yj) или преобразует строку или число в комплексное число
#           EX:
#               x = complex(3, 5)  =>  (3+5j)
# ------------------------------------------------------------------------------
# 17. delattr()      Deletes the specified attribute (property or method) from the specified object
#           RU: Удаляет указанный атрибут (свойство или метод) из указанного объекта
#           EX:
# person = {
#     'name': 'John',
#     'age': 36,
#     'country': 'Norway'
# }
# print(person)
# delattr(person, 'age')
# del person['age']
# print(person)
# ------------------------------------------------------------------------------
# 18. dict()      Returns a dictionary (Array)
#           RU: Возвращает словарь (массив)
#           EX:
# x = dict(name = 'John', age = 36, country = 'Norway')
# ------------------------------------------------------------------------------
# 19. dir()          Returns a list of the specified object's properties and methods
#           RU: Возвращает список свойств и методов указанного объекта
#           EX:
# x = dir(bool)
# print(x)
# [print(z) for z in x]
# ------------------------------------------------------------------------------
# 20. enumerate()  Takes a collection (e.g. a tuple) and returns it as an enumerate object
#           RU: Принимает коллекцию (например, кортеж) и возвращает ее в виде объекта перечисления
#           EX:
# x = ['apple', 'banana', 'cherry']
# y = enumerate(x)
# print(list(y))  # =>  [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# for (index, value) in enumerate(x):
#     print(f'{index} => {value}')

# ------------------------------------------------------------------------------
# 21. float()      Returns a floating point number
# print(float(2)) # => 2.0
# ------------------------------------------------------------------------------
# 22. frozenset()  Returns a frozenset object
# ------------------------------------------------------------------------------
# 23. getattr()      Returns the value of the specified attribute (property or method)
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
# 24. globals()      Returns the current global symbol table as a dictionary
#           RU: Возвращает текущую глобальную таблицу символов в виде словаря
# ex:
# x = 10
# y = 5
# globals = globals()  #=>  []
# print(globals['x'])  #=>  10
# ------------------------------------------------------------------------------
# 25. hasattr()   dictmethod    Returns True if the specified object has the specified attribute (property/method)
#           RU: Возвращает True, если указанный объект имеет указанный атрибут (свойство / метод)
#           EX:
# class Person:
#     name = 'John'
#     age = 36
#     country = 'Norway'
# x = hasattr(Person, 'name') #=> True
# print(x)
# ------------------------------------------------------------------------------
# 26. hash()      Returns the hash value of a specified object
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
# 27. help()      Executes the built-in help system
#           RU: Выполняет встроенную систему справки
#           EX:
#               print(help('modules'))
#               print(help('print'))
#               ...

# ------------------------------------------------------------------------------
# 28. hex()          Converts a number into a hexadecimal value
#           RU: Преобразует число в шестнадцатеричное значение
#           EX:
# x = hex(0)  # => 0x0
# print(x)
# ------------------------------------------------------------------------------
# 29. id()          Returns the id of an object
#           RU: Возвращает идентификатор объекта
#           EX:
# x = ('apple', 'banana', 'cherry')
# print(id(x))  # =>  140714640543488
# print(id(list))
# ------------------------------------------------------------------------------
# 30. input()      Allowing user input
# ------------------------------------------------------------------------------
# 31. int()          Returns an integer number
# ------------------------------------------------------------------------------
# 32. isinstance()  Returns True if a specified object is an instance of a specified object
#           RU: Возвращает True, если указанный объект является экземпляром указанного объекта
#           EX:
#               x = isinstance(5, int)
# is almost similar as type(...)
# RU: почти похоже как type (...)
# ------------------------------------------------------------------------------
# 33. issubclass()  Returns True if a specified class is a subclass of a specified object
#           RU: Возвращает True, если указанный класс является подклассом указанного объекта
#           EX:
# class Person:
#     name = 'John'
#     age = 36

# class Student(Person):
#     grade = 9

# x = issubclass(Student, Person)
# print(x)
# ------------------------------------------------------------------------------
# 34. iter()      Returns an iterator object
#           RU: Возвращает объект итератора
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
#               print(next(x))  =>  cherry
#               print(next(x))  =>  StopIteration
# ------------------------------------------------------------------------------
# 35. len()          Returns the length of an object
# ------------------------------------------------------------------------------
# 36. list()      Returns a list
# ------------------------------------------------------------------------------
# 37. next()      Returns the next item in an iterable
#           RU: Возвращает следующий элемент в итерируемом объекте
#           EX:
#               x = iter(['apple', 'banana', 'cherry'])
#               print(next(x))  =>  apple
#               print(next(x))  =>  banana
# ------------------------------------------------------------------------------
# 38. oct()          Converts a number into an octal
#           RU: Преобразует число в восьмеричное число
#           EX:
#               x = oct(8)  =>  0o10
# ------------------------------------------------------------------------------
# 39. open()      Opens a file and returns a file object
# ------------------------------------------------------------------------------
# 40. ord()       Convert an integer representing the Unicode of the specified character
#           RU: Преобразовать целое число, представляющее Юникод указанного символа
#           EX:
#               x = ord('h')  =>  104

