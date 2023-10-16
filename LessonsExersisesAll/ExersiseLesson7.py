
# 1. Create a tuple with numbers and print one last item.
# RU: Создайте кортеж с числами и выведите один последный элемент.

# def last_element (arr:list):
#     return arr[-1::]
# print(last_element(list(range(1,11))))

# ================================================================

# 2. Create a tuple with numbers and check if a given element exists in the tuple.
# RU: Создайте кортеж с числами и проверьте, существует ли в кортеже заданный элемент.

# def check_if_exists(tup, items_arr):
#     if items_arr in tup:
#         print("yes")
#     else:
#         print("no")
# check_if_exists((1,2,3,4,5,6,7,8,9,100), (100))

# ================================================================

# 3. Create a tuple with numbers and find the index of a given element in the tuple.
# RU: Создайте кортеж с числами и найдите индекс заданного элемента в кортеже.

# def get_index(tup, item):
#     a = tup.index(item)
#     return (f"index of item {item} in tup: {a}")
# print(get_index((1,2,3,4,5,6,7), (3)))

# ================================================================

# 4. Create a tuple with numbers and find the number of occurrences
# of a given element in the tuple.
# RU: Создайте кортеж с числами и найдите количество вхождений заданного
# элемента в кортеж.

# def count_item(tup, item):
#     return tup.count(item)
# print(count_item((1,2,3,4,5,6,1,1,1,1,7), (1)))

# ================================================================

# Write a Python function that takes a tuple of integers as input
# and returns a new tuple with the same integers sorted in descending
# order, but with the even numbers before the odd numbers.
# RU: Напишите функцию Python, которая принимает в качестве входных данных
# кортеж целых чисел и возвращает новый кортеж с теми же целыми числами,
# отсортированными в порядке убывания, но с четными числами перед нечетными.
# INPUT:  => (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
# OUTPUT: => (6, 4, 2, 9, 5, 5, 5, 3, 3, 1, 1)

# def sort_tuple(numbers): 
#     even = [x for x in numbers if x % 2 == 0] 
#     odd = [x for x in numbers if x % 2 != 0] 
#     even.sort(reverse=True)      
#     odd.sort(reverse=True) 
#     return tuple(even + odd)  
# numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5) 
# result = sort_tuple(numbers)  
# print(list(result)) 

# ================================================================
# HOMEWORK

# 1. Write a Python program to sum all the items in a list.





