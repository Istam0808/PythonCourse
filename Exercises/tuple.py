# 1. Create a tuple with numbers and print one last item.
# RU: Создайте кортеж с числами и выведите один последный элемент.
# ================================================================
# 2. Create a tuple with numbers and check if a given element exists in the tuple.
# RU: Создайте кортеж с числами и проверьте, существует ли в кортеже заданный элемент.
def check_if_exists(tup, items_arr):
    obj = {}
    for item in items_arr:
        obj[item] = item in tup
    return all(obj.values())
# print(check_if_exists((1, 2, 3, 4, 5), [1, 5, 4]))
# ================================================================
# 3. Create a tuple with numbers and find the index of a given element in the tuple.
# RU: Создайте кортеж с числами и найдите индекс заданного элемента в кортеже.


def get_index(tup, item):
    return tup.index(item) if item in tup else "Not found"
# print(get_index((1, 2, 3, 4, 5), 10))
# ================================================================
# 4. Create a tuple with numbers and find the number of occurrences
# of a given element in the tuple.
# RU: Создайте кортеж с числами и найдите количество вхождений заданного
# элемента в кортеж.


def count_item(tup, item):
    # return tup.count(item)
    # return len([i for i in tup if i==item])
    result = 0
    for i in tup:
        if i == item:
            result += 1
    return result

# test_tup = (1, 2, 3, 4, 5, 5, 5, 5)
# print(count_item(test_tup, 5))
# ================================================================
# Write a Python function that takes a tuple of integers as input
# and returns a new tuple with the same integers sorted in descending
# order, but with the even numbers before the odd numbers.
# RU: Напишите функцию Python, которая принимает в качестве входных данных
# кортеж целых чисел и возвращает новый кортеж с теми же целыми числами,
# отсортированными в порядке убывания, но с четными числами перед нечетными.
# INPUT:  => (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
# OUTPUT: => (6, 4, 2, 9, 5, 5, 5, 3, 3, 1, 1)


def sort_tuple(tup: tuple) -> tuple:
    evens = [x for x in tup if x % 2 == 0]
    odds = [x for x in tup if x % 2 != 0]
    # evens_sorted = sorted(evens, reverse=True)
    # odds_sorted = sorted(odds, reverse=True)
    evens.sort(reverse=True)
    odds.sort(reverse=True)
    return tuple(evens+odds)


print(sort_tuple((3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)))
