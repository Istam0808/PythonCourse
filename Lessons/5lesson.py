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
"""
"""
for num in range(10, 50, 2):
    print(num) if num % 10 == 0 else print(f'{num} не делиться на 10')



import time 

start = time.time()

def even_nums():
    result = []
    for num in range(1000000):
        result.append(num) if num % 2 == 0 else "It is ODD"
    return result
        
print(even_nums())
end = time.time()
print(f"time take: {round(end - start, 5)}")
"""


