# BUILT IN FUNCTIONS
# =======================================================================================

# 1. Create a function that sums up all the numbers in a list and compare
# it with the highest number from the same list. Then, get the difference and
# show the message that if it is even or odd number.
# RU: Создайте функцию, которая суммирует все числа в списке и сравнивает
# это с самым большим числом из того же списка. Затем получите разницу и
# покажите сообщение, четное это число или нечетное.
from functools import reduce


def sum_and_compare(arr):
    total = sum(arr)
    max_num = max(arr)
    difference = total - max_num
    even_or_odd = 'even' if difference % 2 == 0 else 'odd'
    return f"Total: {total}, Max: {max_num}, Difference: {difference} and it is {even_or_odd}"
# print(sum_and_compare([1, 2, 3, 4, 5]))

# =======================================================================================

# 2. Create a function that takes a list of numbers and returns third biggest.
# RU: Создайте функцию, которая принимает список чисел и возвращает третий по величине.


def third_smallest(list):
    list_copy = list.copy()
    smallest = min(list)
    list_copy.remove(smallest)
    second_smallest = min(list_copy)
    list_copy.remove(second_smallest)
    return min(list_copy)
    # second_highest = min([x for x in list if x != highest])
    # return min([x for x in list if x != highest and x != second_highest])

# =======================================================================================
# 3. Write a program that takes a list of strings as input and returns the longest string.
# RU: Напишите программу, которая принимает список строк в качестве входных
# данных и возвращает самую длинную строку.


def longest_word():
    print(max(input("Enter words separated by comma ',': ").split(','), key=len))

# =======================================================================================
# 4. Write a program that takes a string as input and returns the number of letters in each string.
# RU: Напишите программу, которая принимает строк в качестве входных данных
# и возвращает количество букв в каждой строке.


def letters_in_string():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(map(lambda x: len(x.strip()), words)))

# =======================================================================================
# 5. Write a program that takes a list of numbers as input and
# returns the average of the numbers.
# RU: Напишите программу, которая принимает список чисел в качестве
# входных данных и возвращает среднее значение чисел.
# [13, 22, 35, 41, 52]   => 13+24+35+41+52+5+2 = 170 / 7 = 24.28


def average_of_numbers():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    print(round(sum([int(x.strip()) for x in numbers]) / len(numbers)))

# =======================================================================================
# 6. Write a program that takes a string as input and returns the string with all vowels removed.
# RU: Напишите программу, которая принимает строку в качестве входных
# данных и возвращает строку без гласных.


def words_without_vowels():
    vowels = 'aeiou'
    words = input("Enter words separated by comma ',': ").split(',')

    def remove_vowel(word):
        return "".join([letter for letter in word if letter.lower() not in vowels])
    print(list(map(remove_vowel, words)))

    # words = [x for x in words if x not in vowels]
    # return ''.join(words)


# =======================================================================================
# 7. Write a program that takes a list of strings as input and returns a new list with all strings capitalized.
# RU: Напишите программу, которая принимает список строк в качестве входных данных и возвращает
# новый список со всеми строками прописными.
words = ['AbsAbs', "ObsOO", "PstqR"]


def capitalized_words():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(map(lambda x: x.capitalize(), words)))


def count_caps(words):
    # count = 0
    # for word in words:
    #     for letter in word:
    #         if letter.isupper():
    #             count += 1
    # return count
    # =======================================
    def count_uppers(word):
        return len(list(filter(lambda letter: letter.isupper(), list(word))))
    return sum(list(map(count_uppers, words)))


print(count_caps(words))


# =======================================================================================
# 8. Write a program that takes a list of numbers as input and returns the largest number.
# RU: Напишите программу, которая принимает список чисел в качестве входных данных и возвращает
# самое большое число.


def largest_number():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    print(max(numbers))
    # Using reduce()
    print(reduce(lambda x, y: x if x > y else y, numbers))  # type: ignore

# =======================================================================================
# 9. Write a program that takes a list of strings as input and returns a new list with
# all strings of length 4 or greater.
# RU: Напишите программу, которая принимает список строк в качестве входных данных и возвращает
# новый список со всеми строками длиной 4 или больше.


def words_length():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(filter(lambda x: len(x.strip()) >= 4, words)))

# =======================================================================================

# 10. Write a function that takes a list of integers as input
# and returns the sum of the squares of the even numbers
# in the list. Use the reduce() function to perform the calculation.
# RU: Напишите функцию, которая принимает список целых чисел
# в качестве входных данных и возвращает сумму квадратов четных
# чисел в списке. Используйте функцию reduce() для выполнения вычислений.

# INPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >> 2**2 + 4**2 + 6**2 + 8**2 = 120
# OUTPUT: 120


def sum_of_squares():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    even_nums = map(lambda x: int(x.strip())**2 if int(x) %
                    2 == 0 else 0, numbers)
    print(reduce(lambda x, y: x + y, list(even_nums)))

# =======================================================================================
# =======================================================================================

# 11. Use map() to convert a list of strings to a list of integers.
# RU: Используйте map(), чтобы преобразовать список строк в список целых чисел.

# INPUT:   ["www", "12345", "qwe", 124, '54321', 'aaaaa']
# OUTPUT:  [3, 12345, 3, 124, 54321, 5]


def get_as_nums(arr: list) -> list:

    def get_as_num(val) -> int:
        if type(val) == int:
            return val
        elif val.isnumeric():
            return int(val)
        else:
            return len(str(val))

    return list(map(get_as_num, arr))


test_arr = ["www", "12345", "qwe", 124, '54321', 'aaaaa']
total = get_as_nums(test_arr)
print(total)


# =======================================================================================
# 12. Use filter() to remove all odd numbers from a list.
# RU: Используйте filter(), чтобы удалить все нечетные числа из списка.
def remove_odd_numbers(arr: list) -> list:
    return list(filter(lambda x: x % 2 == 0, arr))


# =======================================================================================
# 13. Use map() and filter() together to convert a list of
# strings to a list of integers and then remove all odd numbers.
# RU: Используйте map() и filter() вместе, чтобы преобразовать
# список строк в список целых чисел, а затем удалить
# все нечетные числа.
def map_and_filter(arr: list) -> list:

    def get_as_num(val) -> int:
        if type(val) == int:
            return val
        elif val.isnumeric():
            return int(val)
        else:
            return len(str(val))

    return list(filter(lambda x: x % 2 == 0,  list(map(get_as_num, arr))))


test_arr = [22, "wwww", "12345", "qwe", 124, '54321', 'aaaaa']
# print(map_and_filter(test_arr))

# =======================================================================================
# 14. Write a function that takes an input from user and deletes all duplicate
# letters using filter or map somehow. Then, count each letter within the original str
# RU: Напишите функцию, которая принимает ввод от пользователя и удаляет все дублирующиеся
# буквы с помощью filter() или map() каким-то образом. Затем подсчитайте каждую букву в исходной строке


def remove_duplicates_and_count_letters():
    sentence = input("Enter a sentence: ")
    total = {}
    letters = []

    def del_duplicates(letter):
        if letter not in letters and not letter.isspace():
            return letters.append(letter.lower())

    list(filter(del_duplicates, list(sentence)))

    print(letters)
    for letter in letters:
        total[letter] = sentence.count(letter)

    print(total)


remove_duplicates_and_count_letters()

# =======================================================================================

# 15. Create a function that can take a list of positive or negative numbers
# and get the difference between smallest positive and largest negative numbers
# Do this with the help of filter or map or reduce.
# Then find nearest number to this difference
# EX:
#   l = [1, -2, 10, 4, 5, -6, 7, 8, 9]
#   distance = 3
#   result = 3nd index that is 4
