# LIST EXERCISES

# 1. Write a Python function that takes a list of words and returns the length
# of the longest one.
# RU: Напишите функцию Python, которая принимает список слов и возвращает
# длину самого длинного слова.
def longest_word(words):  # самое_длинное_слово
    print(max(words, key=len))
    # return max(words, key=lambda x: len(x))


# 2. Write a Python program to count the occurrences of each word in a given sentence.
# RU: Напишите программу Python, чтобы подсчитать количество вхождений каждого слова в заданном предложении.
def count_occurences(string):  # подсчитать_вхождения
    dict = {}
    for i in string.split():
        dict[i] = string.count(i)
    return dict
    # return {i: string.count(i) for i in string.split()}

# 3. Write a Python program to sum all the items in a list.
# RU: Напишите программу Python, чтобы сложить все элементы в списке.


def sum_list(list):  # сложить_список
    return sum(list)


# 4. Write a Python program to multiplies all the items in a list.
# RU: Напишите программу Python, чтобы умножить все элементы в списке.
def multiply_list(list):  # умножить_список
    result = 1
    for i in list:
        result *= i
    return result
    # return [result := result * i for i in list][-1]


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = 1
# [result := result*num for num in arr]
# print(result)


# 5.  Write a Python program to get the largest number from a list.
# RU: Напишите программу Python, чтобы получить наибольшее число из списка.


# 6. Get the largest and smallest numbers of the list and sum both.
# Afterwards, check if the number of the equation is even or odd
# RU: Получите наибольшее и наименьшее числа списка и сложите их.
# После этого проверьте, является ли число уравнения четным или нечетным
# UZ: Ro'yxatning eng katta va eng kichik sonlarini oling va ularni yig'ing.
# Keyin, tenglamani soni juft yoki toq ekanligini tekshiring
def smallest_greatest_sum(arr):
    arr2 = sorted(arr)
    largest = arr2[-1]
    smallest = arr2[0]
    sum = largest + smallest
    if sum % 2 == 0:
        print(f'{sum} is even')
    else:
        print(f'{sum} is odd')

# test_arr = [2, 123, 3, 32, 22, 15]
# smallest_greatest_sum(test_arr)
# ==========================================================================

# 7.  Write a Python program to count the number of strings from a given
# list of strings. The string length is 2 or more and the first
# and last characters are the same.
# RU: Напишите программу Python, чтобы подсчитать количество строк из заданного
# список строк. Длина строки 2 или более, а первые 2 и последние 2 символы одинаковы.
# ['abc', 'xyz', 'aba', '1212381923128321']
# Expected Result : 2


def count_strings(arr):
    result = 0
    for el in arr:
        first_two = el[0:2]
        if first_two[::-1] == el[-2:]:
            result += 1
    return result
    # return len([x for x in z if x[:2] == x[-2:][::-1]])
    # return [el[:2][::-1]==el[-2:] for el in arr].count(True)

# print(count_strings(['abc', 'xyz', 'aba', '1212381923128321']))


# ==========================================================================

# 8. Write a Python program to remove duplicates from a list.
# RU: Напишите программу Python, чтобы удалить дубликаты из списка.
def remove_duplicates(arr):
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result


# =========================================================================
linked_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 9. Merge two singly linked lists without creating new nodes.
# RU: Объедините два односвязных списка без создания новых узлов.


def merge_linked_lists(list1, list2):
    list1.extend(list2)
    return list1

# ==========================================================================
# 10. Find the middle element of the linked list in a single pass.
# RU: Найдите средний элемент связанного списка за один проход.


def middle_element(list):
    return list[len(list) // 2]

# ==========================================================================

# 11. Insert a node in a linked list.
# RU: Вставьте узел в связанный список.


def insert_node(list, node):
    list.append(node)
    return list

# ==========================================================================


# 12. Find the second number of linked lists from the last in a single pass.
# RU: Найдите второе число связанных списков с конца за один проход.
def second_last(list):
    return list[-2]


# ==========================================================================

# 13. Create a function that takes a list of numbers and returns the max value
# using list comprehension
# RU: Создайте функцию, которая принимает список чисел и возвращает максимальное
# значение с использованием генератора списка
def get_max_using_comprehensio(arr):
    pass

# ==========================================================================
# 14. Create a function that takes a list of names and returns the
# ones that start with a vowel.
# RU: Создайте функцию, которая принимает список имен и возвращает те,
# которые начинаются с гласной буквы.


def get_names_starting_with_vowel(arr):
    return [name for name in arr if name[0].lower() in 'aieuo']


# ==========================================================================
# 15. Create a function that takes a list of strings and returns a list with
# only numbers that come after counting the strings that have the letter 'w' in it.
# RU: Создайте функцию, которая принимает список строк и возвращает список с
# только числа, которые идут после подсчета строк, в которых есть буква «w».
def check_w_and_get_length(arr: list[str], letter: str = 'w'):
    # total = []
    # for word in arr:
    #     if letter in word:
    #         total.append(word)
    # return sum([len(x) for x in total])
    # return sum([len(x) for x in [word for word in arr if letter in word]])
    return sum([len(x) for x in list(filter(lambda x: letter in x, arr))])


x = ["hello", "world", "whats", "up", "my", "friend"]
print(check_w_and_get_length(x))


# EX: ['waffle', 'wonderful', 'water', 'phone', 'tree', 'wonderland']
#      => [waffle,  wonderful,  water,  wonderland]  => [6, 9, 5, 10]  =>  30

# ==========================================================================
# 16. Create a function that takes a list of strings and returns a list with
# only the lengths of strings that are divisible by 5.
# RU: Создайте функцию, которая принимает список строк и возвращает список с
# только длины строк, которые делятся на 5.
