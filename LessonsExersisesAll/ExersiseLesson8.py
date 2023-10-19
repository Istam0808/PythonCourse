# BEGINNER LEVEL
# ==========================================================================================

# 1. Create a function that gets only numbers from given sentence and
# separates them into two lists: evens and odds
# RU: Создайте функцию, которая получает только числа из данного предложения и
# разделяет их на два списка: четные и нечетные
# Use at least one built-in function
# RU: Используйте по крайней мере одну встроенную функцию

# INPUT: "Hello 7th World in 2023 year 2nd time"
# [7, 3] [2, 0, 2]

# def even_odd(sentence):
#     numbers = [int(x) for x in sentence.split() if x.isdigit()]
#     even = [x for x in numbers if x % 2 == 0]
#     odd = [x for x in numbers if x % 2 != 0]
#     return even, odd
# even, odd = even_odd("This is a test sentence with 1 2 3 numbers 4 5 6")
# print("Evens:", even)
# print("Odds:", odd)

# ==========================================================================================

# 2. Create a function that accepts a string and counts the number of
# upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# ---------------------------------
# RU: Создайте функцию, которая принимает строку и подсчитывает количество
# прописных и строчных букв.
# Пример строки: 'The quick Brow Fox'
# Ожидаемый результат:
# Количество прописных букв: 3
# Количество строчных букв: 12

# def upper_lower(sentence):
#     upper = 0
#     lower = 0

#     for char in sentence:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1 
#     return f"Количество прописных букв: {upper} \nКоличество строчных букв: {lower}"
# print(upper_lower('The quick Brow Fox'))

# ==========================================================================================

# 3. Create a function that counts vowel and consonant letters in a string.
# RU: Создайте функцию, которая подсчитывает гласные и согласные буквы в строке.

# def vowels_and_constants(sentence):
#     vowels = 0 
#     constants = 0
#     vowels1 = 'A', 'E', 'I', 'O', 'U', 'Y'
#     constants1 = 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'

#     for letter in sentence:
#         if letter.upper() in vowels1:
#             vowels += 1
#         elif letter.upper() in constants1:
#             constants += 1   
#     return f"Гласные буквы в тексте: {vowels} \nСогласные буквы в тексте: {constants}"
# sentence = "ABCDEFG"
# print(vowels_and_constants(sentence))

# ==========================================================================================
# 4. Write a program that takes a list of numbers as input and
# returns the sum of the even numbers.
# RU: Напишите программу, которая принимает список чисел в качестве входных
# данных и возвращает сумму четных чисел.

# def sum_even_nums(nums):
#     even_nums = 0

#     for num in nums:
#         if num % 2 == 0:
#             even_nums += num
#     return even_nums

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_even_nums(nums))

# ==========================================================================================
# 5. Write a Python program to find those numbers which are
# divisible by 7 and multiples of 5, between 1500 and 2700
# (both included).
# RU: Напишите программу на Python для поиска тех чисел,
# которые делятся на 7 и кратны 5, в диапазоне от 1500 до 2700
# (включительно).

# 7 and 5
# 1500 and 2700
def find_numbers():
    pass


# ==========================================================================================

# INTERMEDIATE LEVEL


# 1. Find an average number of given numbers of the list
# and return nearest integer from given list
# RU: Найти среднее число данного списка и вернуть ближайшее
# целое число из данного списка.
# INPUT:  [1, 10, 40, 35, 20, 30, 50, 60, 70]
# OUTPUT: 37.777...  =>  35  =>  index-3
def nearest_average(arr):
    pass

# ==========================================================================================

# 2. Print stars (*) in the shape of a pyramid with N number of steps.
# pyramid(4) =>
#    *
#   ***
#  *****
# *******
def pyramid(n):
    pass


# ==========================================================================================
# 4. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong
# then the prompt appears again until the guess is correct, on successful
# guess, user will get a "Well guessed!" message, and the program will exit.
# ---------------------------------------------------------------
# RU: Напишите программу на Python, чтобы угадать число от 1 до 9.
# Примечание: пользователю предлагается ввести догадку. Если пользователь
# угадывает неправильно, то подсказка появляется снова, пока догадка не будет
# правильной, при успешном угадывании пользователь получит сообщение «Хорошо
# угадано!» и программа выйдет.
def guess_number():
    pass

# ==========================================================================================
# 4. Write a Python program to construct the following pattern,
# using a nested for loop.
# RU: Напишите программу на Python для построения следующего узора,
# используя вложенный цикл for.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
def pattern(n):
    pass
# ==========================================================================================



# 5. Write a program that takes a range of 100 numbers
# and checks if the number is dividible to 3, 5 or both.
# Then takes these numbers and sums them all together
# ----------------------------------------------------
# RU: Программа принимает диапазон 100 чисел и проверяет,
# делится ли число на 3, 5 или на оба. Затем возмите эти числа
# и суммируйте их всех вместе и скажите какое число ЧЁТНОЕ ИЛИ НЕТ.
def сумма_кратных_чисел():
    pass

# ==========================================================================================

# 6. Write a program that prints out the first 100 prime numbers.
# RU: Напишите программу, которая выводит первые 100 простых чисел.
# prime_numbers = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
def n_prime_numbers(n):
    pass

# ==========================================================================================

# 7. Write a program that calculates the sum of the first 1000 Fibonacci numbers.
# RU: Напишите программу, которая вычисляет сумму первых 1000 чисел Фибоначчи.
def sum_fibonacci(n):
    pass

# ==========================================================================================

# 8. Write a program that generates a random password of length 20.

# import random 

# def create_password_of_length():
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     letters_ru = "абвгдеёжз"
#     numbers = "1234567890"
#     symbols = "!@#$%^&()_+<>?/;:"
#     total_sybols_for_password = 20

#     everything_includes = letters + letters_ru + numbers + symbols
#     created_password = ""

#     for i in range(total_sybols_for_password):
#         random_int = random.randint(0, len(everything_includes)-1)
#         created_password += everything_includes[random_int]
#     print(created_password)
# create_password_of_length()
# ==========================================================================================