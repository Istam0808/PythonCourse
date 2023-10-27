# 8. Write a Python program to remove a key from a dictionary.
# RU: Напишите программу Python для удаления ключа из словаря.

# def remove_key(dc, key):
#     if key in dc:
#         dc.pop(key)    
#     return dc
# print(remove_key({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'a'))
# ==============================================================

# 9. Write a Python program to sort a given dictionary by key.
# RU: Напишите программу Python для сортировки заданного словаря по ключу.

# def sort_dict_by_key(d):
#     sorted(d.items())
#     return dict(sorted(d.items()))
# print(sort_dict_by_key({'d': 4,  'b': 2, 'a': 1, 'c': 3 }))

# ==============================================================
# 10. Write a Python program to get the maximum and minimum value in a dictionary.
# RU: Напишите программу Python, чтобы получить максимальное и минимальное значение в словаре.
# ex: {'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}

# def get_max_min(dict):
#     maxi = max(dict.values())
#     mini = min(dict.values())
#     return (f"MAX Value in dict: {maxi}\nMIN Value in dict: {mini}")
# print(get_max_min({'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}))

# ==============================================================
# 11. Write a Python program to remove duplicates from the dictionary.
# First, leave at least one item from duplicates
# Second, delete all duplicates
# RU: Напишите программу Python для удаления дубликатов из словаря.
# Во-первых, оставьте хотя бы один элемент из дубликатов
# Во-вторых, удалите все дубликаты
# ex: {'x':1, 'y':2, 'z':2, 'a':3, 'b':1, 'c':3}
# =>  {x':1, 'y':2, 'a':3}

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

# ==============================================================
# 12. Write a function that takes a dict as first argument and number as second argument.
# Return a list of all the keys that have values greater than the number passed as second argument.
# RU: Напишите функцию, которая принимает словарь в качестве первого аргумента и число в
# качестве второго аргумента. Верните список всех ключей, у которых значения больше, чем число,
# переданное в качестве второго аргумента.
# Input:   {'a': 100, 'b': 200, 'c': 300, 'd': "Hello world", 'e': True},    150
# Output:  {'b': 200, 'c': 300}
def get_keys_greater_than(dict, num):
    pass


# ==============================================================
# 14. Write a function that takes a dictionary as an argument and returns
# a new dictionary with the keys and values reversed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента
# и возвращает новый словарь с обратными ключами и значениями.

# def reverse_dict(d):
#     a = {v:k for k,v in d.items()}
#     return a 
# print(reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}))

# ==============================================================
# 15. Write a function that takes a list of dictionaries as an argument
# and returns a sum of numeric values of all dicts
# RU: Напишите функцию, которая принимает список словарей в качестве аргумента
# и возвращает сумму числовых значений всех словарей
# x = {'a': 1, 'b': "2", "c": "Hello"}
# z = {'d': "4", 'e': 3, "f": "World"}
# a = {'g': 5, 'h': "!!!", "i": "6"}
# arr = [x, z, a]
# # test(arr)  #  21
# def sum_numeric_values(arr_of_dicts: list[dict]) -> int:
#     pass

# ==============================================================
# 16. Write a function that takes a dictionary as an argument and returns a new
# dictionary that contains only the key-value pairs where the value is a string.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента и возвращает
# новый словарь, который содержит только пары ключ-значение, где значение - строка.

# x = {1: 1, 2: 2, 3: "Hello"}
# a = {v for v in x.values() if isinstance(v, str)}
# print(a)