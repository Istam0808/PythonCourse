#1. Напишите программу на Python для вычисления длины строки.

# def calculate_string (string):
#     return(len(string))
# print(calculate_string('istam'))
#---------------------------------------------------------------------------------------

#2. Напишите программу на Python для подсчета количества символов (частоты символов) в строке.
# Пример строки: google.com.
# Ожидаемый результат: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm' : 1}

# def count_characters (string):
#     dict = {}
#     for i in string:
#         keys = dict.keys()
#         if i in keys:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
# print(count_characters('Istam_122'))
#---------------------------------------------------------------------------------------

#3. Напишите программу на Python, чтобы получить строку, состоящую из первых двух и последних двух символов заданной строки. Если длина строки меньше 2, вместо этого верните пустую строку.
# Пример строки: 'w3resource'
# Ожидаемый результат: 'w3ce'
# Пример строки: 'w3'
# Ожидаемый результат: 'w3w3'
# Пример строки: 'w'
# Ожидаемый результат: пустая строка

#1
# def string_first_and_last_two_letters (string):
#     return(string[:2:] + string[5::])
# print(string_first_and_last_two_letters('i3stam3'))

#2
# def string_first_and_last_two_letters(string):
#   if len(string) < 2:
#     return ''
#   return string[0:2] + string[-2:]

# print(string_first_and_last_two_letters('Istam'))
# print(string_first_and_last_two_letters('I2'))
# print(string_first_and_last_two_letters('I'))
#---------------------------------------------------------------------------------------

# 4. Напишите программу на Python, чтобы получить строку из заданной строки, в которой все вхождения ее первого символа были изменены на «$», за исключением самого первого символа.
# Пример строки: «restart».
# Ожидаемый результат: «resta$t».

# def update_character(string):
#     char = string[0]
#     string = string.replace(char, '$')
#     string = char + string[1::]
#     return string
# print(update_character('istaiimii'))
#---------------------------------------------------------------------------------------

# 5. Напишите программу на Python, чтобы получить одну строку из двух заданных строк, разделенных пробелом, и поменять местами первые два символа каждой строки.
# Пример строки: «abc», «xyz».
# Ожидаемый результат: «xyc abz».

# def fifth_ex (string, string1):
#     new_string = string1[:2] + string[2:]
#     new_string1 = string[:2] + string1[2:]
#     return new_string + ' ' +new_string1
    
# print(fifth_ex('abc','der'))
#---------------------------------------------------------------------------------------

# 6. Напишите программу на Python, добавляющую «ing» в конец заданной строки 
# (длина должна быть не менее 3). Если данная строка уже заканчивается на «ing», 
# добавьте вместо нее «ly». Если длина данной строки меньше 3, оставьте ее без изменений.
# Пример строки: 'abc'
# Ожидаемый результат: 'abcing'
# Пример строки: 'string'
# Ожидаемый результат: 'stringly'

# def last_ing (string):
#     simb = len(string)
#     if simb < 3:
#         return string
#     elif string[-3:]== 'ing':
#         return string + 'ly'
#     else:
#         return string + 'ing'
# print(last_ing('istam'))
#---------------------------------------------------------------------------------------

# 8. Напишите функцию Python, которая принимает 
# список слов и возвращает самое длинное слово и длину самого длинного слова.
# Пример вывода:
# Самое длинное слово: Упражнения
# Длина самого длинного слова: 9.

# def max_word (string_list):
#     a = []
#     for i in string_list:
#         a.append((len(i), i))
#     a.sort()
#     return a[-1][0], a[-1][1]
# result = max_word(["shaxa", "istam", "pythonnomberone"])
# print("max:",result[1])
# print("len_max:",result[0])
#---------------------------------------------------------------------------------------

# 9. Напишите программу на Python для удаления n-го 
# индексного символа из непустой строки.

# def remove_nth_index(string, index):
#     return(string [:index] + string[index +1:])
# print(remove_nth_index('istam',2))
#---------------------------------------------------------------------------------------

# 10. Напишите программу Python для изменения заданной строки на новую строку, 
# в которой первый и последний символы поменялись местами.

# numbers = [1, 2, 3, 4, 5]
# numbers[0], numbers[-1] = numbers[-1], numbers[0]
# print(numbers)
#---------------------------------------------------------------------------------------

# 11. Напишите программу на Python для удаления символов, 
# имеющих нечетные индексные значения в данной строке.

# string = "123456789"
# string1 = ""
# for i in range(len(string)):
#     if i % 2:
#         string1 += string[i]
# print(string1)  
#---------------------------------------------------------------------------------------

# 12. Напишите программу на Python для подсчета вхождений 
# каждого слова в заданном предложении.

# def count_characters (string):
#     dict={}
#     for i in string.split(' '):
#         dict=dict|{i:string.split(' ').count(i)}
#     return dict
# print(count_characters('Istam12 fdgfg fgdd fgdd'))
#---------------------------------------------------------------------------------------

# 13. Напишите сценарий Python, который принимает вводимые пользователем
# данные и отображает их обратно в верхнем и нижнем регистре.

# def cases (string):
#     user_input = input('please write text: ')
#     a = user_input.lower()
#     b = user_input.upper()
#     return (f"lower text {a} , Upper text {b}")
# print(cases('string'))
#---------------------------------------------------------------------------------------

# 14. Напишите программу на Python, которая принимает на вход 
# последовательность слов, разделенных запятыми, 
# и печатает отдельные слова в отсортированной форме (буквенно-цифровом формате).
# Примеры слов: red, black, pink, green.
# Ожидаемый результат: black, green, pink, red.

# def sort_words():
#     items = input("напишите слова с запятой: ")
#     words = [word for word in items.split(",")]
#     sorted_words = sorted(list(set(words)))
#     return ",".join(sorted_words)
# print(sort_words())
#---------------------------------------------------------------------------------------

# 16. Напишите функцию Python для вставки строки в середину строки.
# Пример функции и результат:
# Insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# Insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

# def center_text(str, word):
# 	return str[:3] + word + str[3:]\
# print(center_text('[[[]]]', 'Python'))
# print(center_text('{{{}}}', 'C++'))
# print(center_text('<<<>>>', 'HTML'))
#---------------------------------------------------------------------------------------

# 17. Напишите функцию Python, чтобы получить строку, состоящую из 4
# копий последних двух символов указанной строки (длина должна быть не менее 2).
# Пример функции и результата:
# Insert_end('Python') -> onononon
# Insert_end('Упражнения') -> eseseses

# def string_last_two(string):
#     return string + string[-2::] *4
# print(string_last_two('Python'))
#---------------------------------------------------------------------------------------

# 18. Напишите функцию Python для получения строки, 
# состоящей из первых трех символов указанной строки. 
# Если длина строки меньше 3, верните исходную строку.
# Пример функции и результата:
# first_three('ipy') -> ipy
# first_three('python') -> pyt

# def first_three(string):
#     if len(string) < 3:
#         return string
#     else:
#         return string + string[:3] * 3
# print(first_three("Python"))
#---------------------------------------------------------------------------------------

# 20. Напишите функцию Python для переворачивания строки, 
# если ее длина кратна 4.

# def revers_text(string):
#     if len(string) % 4 == 0:
#         return ''.join(reversed(string))
#     return string 
# print(revers_text("ista"))
# print(revers_text("istam"))
#---------------------------------------------------------------------------------------
