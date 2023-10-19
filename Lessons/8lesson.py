# import time
# start_time = time.time()
# for i in range(10):
#     for i2 in range(10):
#         print(i2)
# end_time = time.time()
# a = "Taken time:", round(end_time - start_time, 10)
# print(a)

#-------------------------------------------------------------------------------

# itr1 = ['a','b','c']
# itr2 = [1,2,3]
# itr3 = ['x', 'y','z']
# zipped_itr = zip(itr1,itr2,itr3)
# # print(list(zipped_itr))
# for first,second,third in zipped_itr:
#     print(first,second,third)

#-------------------------------------------------------------------------------
# import random 
# letters = "abcdefghijklmnopqrstuvwxyz"
# letters_ru = "абвгдеёжз"
# numbers = "1234567890"
# symbols = "!@#$%^&()_+<>?/;:"
# total_sybols_for_password = 20

# everything_includes = letters + letters_ru + numbers + symbols
# created_password = ""

# for i in range(total_sybols_for_password):
#     random_int = random.randint(0, len(everything_includes)-1)
#     created_password += everything_includes[random_int]
# print(created_password)

#-------------------------------------------------------------------------------

# test_obj = { 1:'a', 2:'b', 3:'c'}
# ---------------------------------------------------------
# In JS
# Object.keys(my_obj), Object.values(my_obj), Object.entries(my_obj)
# ---------------------------------------------------------
# In Python
# my_obj.keys(), my_obj.values(), my_obj.items()
# ---------------------------------------------------------
# for value in test_obj.values():
#     print(value)
# for key in test_obj.keys():
#     print(key)
# for key, value in test_obj.items():
#     print(key, value)

# ----------WHILE LOOP
# SYNTAXIS
# condition = 2==2
# while condition == True:
    # do something

# ----------FOR LOOP
# SYNTAXIS
# for x in []:
#   print(x)
# ----------ENUMERATE
# enumerate is used to get an index for the item that we are taking from list
# ex:
#   for index, item in enumerate(list):
#       print(index, item)
# ---------------------------------------------------------
# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# for idx, item in enumerate(arr):
#     print(idx, item)

# ==============================================================================
# break     => breaks up the current loop
# RU: прерывает текущий цикл
# continue  => skips the current iteration of the loop
# RU: пропускает текущую итерацию цикла
# ---------
# fruits = ["apple", "banana", "kiwi", "mango", "disgusting cherry", "kiwi", "mango"]
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
# ---------------------------------------------------------
# import time
# start_time = time.time()
# for i in range(10):
#     for i2 in range(10):
#         print(i2)
# end_time = time.time()
# print("Time taken: ", round(end_time - start_time, 4))
# ---------------------------------------------------------
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
# for i in range(10):
#     pass
# for i in "Some text":
#     pass
# ==================================================================
# itr1 = list('abcdefghijklmnopqrstuvwxyz') 
# itr2 = range(len(itr1))
# itr3 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 
#         'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 
#         'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 
#         'ю', 'я']

# zipped = zip(itr2, itr3)
# for (letter, number) in zipped:
#     print(letter, number)
# ==================================================================
# itr1 = ['a', 'b', 'c']
# itr2 = [ 1,   2,   3,  4 ]
# itr3 = ['x', 'y', 'z', 'w', 'u']
# zipped_itr = zip(itr1, itr2, itr3)

# for first, second, third in zipped_itr:
#     print(first, second, third)

# ==================================================================
# loop with dictionaries
# for key, value in dict.items():
#     print(key, value)
# ==================================================================
