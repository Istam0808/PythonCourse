# INITIAL SETS

odds = {1, 3, 5}
evens = {0, 2, 5, 6, 7}
primes = {2, 3, 5, 7, 11}
fibonacci = {1, 1, 2, 3, 5, 8, 13}


# =====================================================================================================
# =====================================================================================================

# 1. Create two sets and merge them into one set.
# RU: Создайте два множества и объедините их в одно множество.
set3 = odds.union(evens)
# print(set3)


# =====================================================================================================
# =====================================================================================================

# 2. Create two sets and exclude the intersection of sets from one set.
# RU: Создайте два сета и исключите пересечение сеты из одного сета.
set4 = odds.difference(evens, {1, 3, 5})
# print(set4)

# =====================================================================================================
# =====================================================================================================

# 3. Create two sets and compare them. Print the result of comparing the sets.
# RU: Создайте два сета и сравните их. Распечатайте результат сравнения сетов.
set5 = odds.symmetric_difference({1, 3, 5})
# print(set5)

# =====================================================================================================
# =====================================================================================================

# 4. Create two sets and print the result of their intersection.
# RU: Создайте два сета и распечатайте результат их пересечения.
set6 = odds.intersection({1, 3, 5})
# print(set6)


# =====================================================================================================
# =====================================================================================================

# 5. The students of District College have subscriptions to English and
# French newspapers. Some students have subscribed only to English, some
# have subscribed to only French and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to
# the English newspaper, and the other set is subscribed to the French newspaper.
# The same student could be in both sets. Your task is to find the total number of
# students who have subscribed to at least one newspaper.
# ------------------------------------------------------
# RU: У студентов District College есть подписки на английские и французские газеты.
# Некоторые студенты подписались только на английский, некоторые подписались только на французский,
# а некоторые подписались на обе газеты.
# Вам даны два набора номеров роллов студентов. Один набор имеет подписку на английскую газету,
# а другой набор подписан на французскую газету. Один и тот же студент может быть в обоих наборах.
# Ваша задача - найти общее количество студентов, которые подписались хотя бы одну газету.
def total_subscriptions(set1, set2):
    return len(set1.union(set2))


# =====================================================================================================
# =====================================================================================================

# 6. Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of
# the room numbers for all of the tourists. The room numbers will appear K times per group
# except for the Captain's room.
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.
# ------------------------------------------------------
# RU: Г-н Анант Асанхья - менеджер отеля INFINITE. В отеле бесконечное количество номеров.
# Однажды прекрасного дня конечное число туристов приезжает остановиться в отеле.
# Туристы состоят из:
# → Капитан.
# → Неизвестная группа семей, состоящая из K человек в группе, где K ≠ 1.
# Капитану был выделен отдельный номер, а остальным - по одному номеру на группу.
# У г-на Ананта есть неупорядоченный список случайно расположенных записей номеров комнат.
# Список состоит из номеров комнат для всех туристов. Номера комнат будут появляться K раз на группу,
# кроме комнаты капитана.
# Г-н Анант нуждается в вашей помощи, чтобы найти номер комнаты капитана.
# Общее количество туристов или общее количество групп семей вам неизвестно.
# Вы знаете только значение K и список номеров комнат.
# ------------------------------------------------------
#

def captain_room(rooms, k):
    # With the help of for loop
    for i in set(rooms):
        if rooms.count(i) == 1:
            return i

    # With the help of comprehension
    # return ((sum(set(rooms)) * k) - (sum(rooms))) // (k - 1)


# EXPLANATION:
    # input:
    # k = 5
    # rooms = 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# OUTPUT:
    # 8
rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3,
         2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
k = 5
# print(captain_room(rooms, k))

# Список номеров комнат содержит 31 элемент. Поскольку K равно 5, должно быть 6 групп семей.
# В данном списке все числа повторяются 5 раз, кроме номера комнаты 8.
# Следовательно, 8 - это номер комнаты капитана.

# =====================================================================================================
# =====================================================================================================

# 7. Write a Python program to remove item(s) from set
# RU: Напишите программу на Python, чтобы удалить элемент(ы) из набора.


def remove_item(set1, *args):
    # for i in args:
    #     set1.remove(i)
    # return set1
    # --------------------
    # Comprehension
    return set1.difference(args)


print(remove_item({'a', 'b', 'c'}, 'c', 'b'))

# =====================================================================================================
# 8. Create a function that takes a list as an argument and creates a set from it
# The result must contain only unique values from the list that are doubled.
# RU: Создайте функцию, которая принимает список в качестве аргумента и с
# оздает из него набор.
# Результат должен содержать только уникальные значения из списка, которые удваиваются.
# Input [1, 3, 4, 1, 2, 4, 5, 3, 2, 4, 1, 'a', 'b', 'c', 'a', 'b', 'c']
# Output {2, 4, 6, 8, 10, 'aa', 'bb', 'cc'}
# {... for ... in {} if ...}


def set_from_list(list1):
    # Comprehension
    # return {i*2 for i in set(list1)}
    # --------------------
    # With the help of loop
    result_set = set()
    for i in list1:
        result_set.add(i*2)
    return result_set
# =====================================================================================================
# 9. Create a function that takes a dict as an arg and gets all values from it and
# converts them into set. Then, plus them all together and return the result by
# saying "The sum is: {sum} and it is {even/odd} number"
# RU: Создайте функцию, которая принимает словарь в качестве аргумента и получает
# все значения из него и преобразует их в набор. Затем сложите их все вместе и
# верните результат, сказав "Сумма равна: {сумма} и это {четное/нечетное} число"
# Input {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'g': 3}
# Output The sum is: 10 and it is even number


def sum_of_values(dict1):
    # Comprehension
    # return f"The sum is: {sum({i for i in dict1.values()})} and it is {'even' if sum({i for i in dict1.values()})%2 == 0 else 'odd'} number"
    # --------------------
    # With the help of Loop
    sum = 0
    for i in dict1.values():
        sum += i
    return f"The sum is: {sum} and it is {'even' if sum%2 == 0 else 'odd'} number"


# =====================================================================================================
# 10. Create a function that takes a list and a number as a target.
# Find two numbers from that list that when summed up are equal to target.
# RU: Создайте функцию, которая принимает список и число в качестве цели.
# Найдите два числа из этого списка, которые в сумме равны цели.
x = [1, 4, 11, 114, 12, 24, 55]
target = 23


def find_target(arr, target):
    for item in arr:
        for item2 in arr:
            item1_index = arr.index(item)
            item2_index = arr.index(item2)
            sum = item + item2
            if item != item2 and item1_index != item2_index and sum == target:
                print(item1_index, item2_index)
                return


find_target(x, target)

# =============================================================


def del_duplicate_vals_from_dict(dict: dict) -> dict:
    """
        We should use set() to remove duplicate values from dictionary
    """
    result = {}
    set_vals = set(dict.values())
    for key, val in dict.items():
        if val in set_vals and val not in result.values():
            result[key] = val
    return result
