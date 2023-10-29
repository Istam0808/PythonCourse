#1

# def mulyply_list(list1):
#     result = 1
#     for i in list1:
#             result *= i
#     return result
# print(mulyply_list([1,2,3]))

#2

# def smallest_greatesr_sum(arr):
#     max1 = max(arr)
#     min1 = min(arr)
#     res = max1 + min1
#     if res %2 == 0:
#         print(f"summa чисел {max1} i {min1} четный")
#     else:
#         print(f"summa чисел {max1} i {min1} нечетный")
# smallest_greatesr_sum([1,2,3])

#3

# def count_strings(arr):
#     result = []
#     for i in arr:
#         a = i[0:2]
#         if a[::-1] == i[-2:]:
#             result.append(i)
#     return f"Result: {result}"
# print(count_strings(['abc', 'xyz', 'aba', '1212381923128321', 'istammatsi']))

#4

# def sort_tuple(tup:tuple):
#     evens = [x for x in tup if x % 2 == 0]
#     odds = [x for x in tup if x % 2 != 0]
#     evens.sort(reverse=True)
#     odds.sort(reverse=True)
#     return tuple(evens+odds)
# print(sort_tuple((3,1,4,1,5,9,2,6,5,3,5)))

#5

# def remove_key(dc, _key):
#     dc_copy = dc.copy()
#     dc_copy.pop(_key)
#     return dc_copy
# print(remove_key(dict(a =1,b = 2,c = 3),'a'))    

#6

# 6. Write a Python program to remove duplicates from the dictionary.
# First, leave at least one item from duplicates
# Second, delete all duplicates
# RU: Напишите программу Python для удаления дубликатов из словаря.
# Во-первых, оставьте хотя бы один элемент из дубликатов
# Во-вторых, удалите все дубликаты
# def remove_duplicates(dict):
    
# def remove_duplicates(dict):
#     result = {}
#     values = []
#     for k, v in dict.items():
#         if v not in values:
#             result[k] = v
#             values.append(v)
#     return result
# new_dict = remove_duplicates({'x':1, 'y':2, 'z':2, 'a':3, 'b':1, 'c':3})
# print(new_dict)

# ex: {'x':1, 'y':2, 'z':2, 'a':3, 'b':1, 'c':3}
# =>  {x':1, 'y':2, 'a':3}

# ==========================================================================
# 7. Write a function that takes a dict as first argument and number as second argument.
# Return a list of all the keys that have values greater than the number passed as second argument.
# RU: Напишите функцию, которая принимает словарь в качестве первого аргумента и число в
# качестве второго аргумента. Верните список всех ключей, у которых значения больше, чем число,
# переданное в качестве второго аргумента.
# Input:   {'a': 100, 'b': 200, 'c': 300, 'd': "Hello world", 'e': True},    150
# Output:  {'b': 200, 'c': 300}

# def get_keys_greater_than(dict, num):
#     a = {k:v for k,v in dict.items() if isinstance(v , int) and v > num} 
#     return a    
# print(get_keys_greater_than({'a': 100, 'b': 200, 'c': 300, 'd': "Hello world", 'e': True},150))

# ==========================================================================
# 8. Write a function that takes a dictionary as an argument and returns
# a new dictionary with the keys and values reversed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента
# и возвращает новый словарь с обратными ключами и значениями.

# def reverse_dict(d):
#     a ={v:k for k,v in d.items()}
#     return a
# print(reverse_dict({"a":1, "b":2}))

# ==========================================================================
# 9. Write a function that takes a list of dictionaries as an argument
# and returns a sum of numeric values of all dicts
# RU: Напишите функцию, которая принимает список словарей в качестве аргумента
# и возвращает сумму числовых значений всех словарей
# x = {'a': 1, 'b': "2", "c": "Hello"}
# z = {'d': "4", 'e': 3, "f": "World"}
# a = {'g': 5, 'h': "!!!", "i": "6"}
# arr = [x, z, a]
# # test(arr)  #  21

# x = {'a': 1, 'b': "2", "c": "Hello"}
# z = {'d': "4", 'e': 3, "f": "World"}
# a = {'g': 5, 'h': "!!!", "i": "6"}
# arr = [x, z, a]

# def sum_numeric_values(arr_of_dicts):
#     total = 0
#     for dict in arr_of_dicts:
#         for val in dict.values():
#             if str(val).isnumeric():
#                 total += int(val)
#     return total
# print(sum_numeric_values(arr))














