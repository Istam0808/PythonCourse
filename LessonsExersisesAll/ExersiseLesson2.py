# # 14. Write a Python function to create an HTML string with tags around the word(s)
# # RU: Напишите функцию Python для создания HTML-строки с тегами вокруг слова (слов).

# def add_tags(tag, word):
# 	return (f'<{tag}>{word}</{tag}>')
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python'))
#---------------------------------------------------------------------------------------
# # 15. Write a Python function to insert a string in the middle of a string.
# # RU: Напишите функцию Python для вставки строки посередине строки.
# # вставить_строку_посередине

# def center_string(string):
#     return (string.center(11, '*'))
# print(center_string(input('>>>')))
#---------------------------------------------------------------------------------------

# # 16. Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из 4 копий последних двух символов заданной строки

# def insert_string_middle(string):
#     last_two = string[-2:]
#     result = last_two * 4
#     return result
# print(insert_string_middle('Middle'))  
#---------------------------------------------------------------------------------------

# # 17. Write a Python function to get a string made of the first three characters of a specified string.
# # If the length of the string is less than 3, return the original string.
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из первых трех символов заданной строки.
# # Если длина строки меньше 3, вернуть исходную строку.

# def first_three(string):  # первые_три
#     return string[:3:] * 3   #+ string[3::]
# print(first_three('ISTAM'))
#---------------------------------------------------------------------------------------

# # 18. Write a Python function to get the first half of a specified string of even length.
# # RU: Напишите функцию Python, чтобы получить первую половину заданной строки четной длины.

# def add_nums(nums):
#     return (nums[1::2] + nums[::2])
# print(add_nums('123456789'))
#---------------------------------------------------------------------------------------

# # 19. Write a Python program to concatenate two strings and return the result.
# # If the length of the strings are not same then remove the characters from the longer string.
# # RU: Напишите программу на Python для объединения двух строк и верните результат. Если длины строк не одинаковы,
# # то удалите символы из более длинной строки.

# def concat_strings(str1, str2):
#     len1 = len(str1)
#     len2 = len(str2)
#     min_len = min(len1, len2)
#     concated_str = str1[:min_len] + str2[:min_len]
#     return concated_str
               
# string1 = input(">>1>>: ")
# string2 = input(">>2>>: ")
# result = concat_strings(string1, string2)
# print("result:", result)
#---------------------------------------------------------------------------------------


# # 20. Write a Python function to convert a given string to all uppercase if it contains
# # at least 2 uppercase characters in the first 4 characters.
# # RU: Напишите функцию Python для преобразования заданной строки в верхний регистр, если она содержит
# # не менее 2 заглавных символов в первых 4 символах.
        
# def convert_to_uppercase(string):
#     count = 0
#     for char in string[:4]:
#         if char.isupper():
#             count += 1
#     if count >= 2:
#         return string.upper()
#     else:
#         return string        
# print(convert_to_uppercase('Hello world'))
# print(convert_to_uppercase('HEllo world'))
# print(convert_to_uppercase('HELlo world'))
#---------------------------------------------------------------------------------------

# # 21. Write a Python program to remove a newline in Python.
# # RU: Напишите программу на Python, чтобы удалить перевод строки в Python.

# def remove_newline(string):  
#     return (string.splitlines())
# print(remove_newline("Istam\n 1Istam\n"))
#---------------------------------------------------------------------------------------

# # 22. Write a Python program to remove existing indentation from all of the lines in a given text.
# # RU: Напишите программу на Python для удаления существующего отступа из всех строк в заданном тексте.

# def remove_indentation(string): 
#     return string.replace(' ' , '') 
# print(remove_indentation("Istam 1istam 2istam 3istam"))
#---------------------------------------------------------------------------------------

# 23. Write a Python program to count and display the vowels of a given text.
# RU: Напишите программу Python, чтобы подсчитать и отобразить гласные заданного текста.

# def count_vowels(*strings):  
#     vowels = ["A", "E", "I", "O", "U", "Y","a","e","i","o","u","y"] 
#     count = 0
#     for string in strings:
#         for letter in string:
#             if letter in vowels:
#                 count += 1
#     return count
# print (count_vowels('i'  ,'st',  'a'   ,'m'   ,'a'   ,'k',   'e'))
#---------------------------------------------------------------------------------------

# 24. Swapkeys

# def swap_cases(string = 'iSTAM_aKE'):  # поменять_регистр
#     return string.swapcase()
# print(swap_cases())
#---------------------------------------------------------------------------------------


# # 25. Write a function in Python to check duplicate letters.
# # It must accept a string, i.e., a sentence. The function should return
# # True if the sentence has any word with duplicate letters, else return False.
# # RU: Напишите функцию на Python для проверки повторяющихся букв.
# # Он должен принимать строку, то есть предложение. Функция должна возвращать
# # True, если в предложении есть слово с повторяющимися буквами, иначе возвращать False.
# # проверить_повторяющиеся_буквы
# def check_duplicate_letters(string) -> bool:


# # 26. Write a function that takes a sentence as argument, then takes last word's first letter and
# # repeats 5 times in the beginning of the sentence and at the end.
# # RU: Напишите функцию, которая принимает предложе0ние в качестве аргумента, затем берет первую букву
# # последнего слова и повторяет 5 раз в начале предложения и в конце.
# def repeat_first_l_of_last_word(sentence):



# # 26. Write a code in Python to create a Morse code translator.
# # You can take a string with alphanumeric characters in lower or upper case.
# # The string can also have any special characters as a part of the Morse code.
# # Special characters can include commas, colons, apostrophes, exclamation marks,
# # periods, and question marks. The code should return the Morse code that is equivalent to the string.
# def morse_code(string):





# # 27. Write a function to detect 13th Friday. The function can accept two parameters,
# # and both will be numbers. The first parameter will be the number indicating the month,
# # and the second will be the year in four digits. Your function should parse the parameters,
# # and it must return True when the month contains a Friday with the 13th, else return False.
# def detect_13th_friday(month, year):



# # 28. Write a function to find the domain name from the IP address. The function will accept an
# # IP address, make a DNS request, and return the domain name that maps to that IP address while
# # using records of PTR DNS. You can import the Python socket library.
# def find_domain_name(ip_address):



# # 29. Write a function in Python to convert a decimal to a hex. It must accept a string of ASCII
# # characters as input. The function should return the value of each character as a hexadecimal string.
# # You have to separate each byte by a space and return all alpha hexadecimal characters as lowercase.
# def convert_to_hex(string):


# # 30. Write a function in Python to parse a string such that it accepts a parameter- an encoded string.
# # This encoded string will contain a first name, last name, and an id. You can separate the values
# # in the string by any number of zeros. The id will not contain any zeros. The function should return
# # a Python dictionary with the first name, last name, and id values. For example, if the input would
# # be "John000Doe000123". Then the function should return:
# # { "first_name": "John", "last_name": "Doe", "id": "123" }
# def encoded_string(string):


# # 31. Write a code in Python to find out whether a given string S is a valid regex or not.
# def is_valid_regex(string):

#---------------------------------------------------------------------------------------

# # 32. Create a function that takes a text and repeats the middle
# # letter three times
# # RU: Создайте функцию, которая принимает текст и повторяет
# # среднюю букву три раза
# # Welcome   =>   Welcccome

# def repeat_middle_letter(string):
#     x = string[:(len(string)//2)] + string[(len(string)//2)]*2 + string[(len(string)//2):] 
#     return x
# text = "ApilL"
# result = repeat_middle_letter(text)
# print(result)
#---------------------------------------------------------------------------------------

# # 33. Create a function that repeats first and last half of the text n times
# # RU: Создайте функцию, которая повторяет первую и вторую половину текста n раз
# # "Welcome"  =>  "WelWelWelcomecomecomecome"

def repeat_half_n_times(sen ,n):
    x=(sen[0:round(len(sen)/2)])*n+(sen[round(len(sen)/2):])*n
    print(x)
repeat_half_n_times('qwertyuio',2)
#---------------------------------------------------------------------------------------











































