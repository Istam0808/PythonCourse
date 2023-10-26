# def count_letters(lst):
#     count_char = {}
#     for char in lst:
#         if char in count_char:
#             count_char[char] += 1
#         else:
#             count_char[char] = 1
#     for letter, count_char in count_char.items():
#         print(letter, "=", count_char)

# count_letters("Istamrustam")


# def test (string):
#     res = ''
#     for index ,i in enumerate(string):
#         if index % 2 == 0:
#             res+=i.upper()
#             continue
#         res+=i.lower()
#     return res

# print(test("istam"))


# 2. Напишите программу на Python, чтобы создать
# функцию, которая принимает один аргумент, и этот 
# аргумент будет умножен на неизвестное заданное число.
# Пример вывода:
# Удвойте число 15 = 30.
# Утроите число 15 = 45.
# Увеличьте число 15 в четыре раза = 60.
# Увеличьте число в пять раз. 15 = 75.


# def nums(nums):
#     a = nums * 2
#     b = nums * 3
#     c = nums * 4
#     d = nums * 5
#     print (f"Удвойте число {nums} = {a}\nУтроите число {nums} = {b}\nУвеличьте число {nums} в четыре раза = {c}\nУвеличьте число в пять раз {nums} = {d}")
# nums(15)

# ↓↓↓↓↓↓↓ This task with lambda ↓↓↓↓↓↓↓
# def func_compute(n):
#  return lambda x : x * n
# result = func_compute(2)
# print("Double the number of 15 =", result(15))
# result = func_compute(3)
# print("Triple the number of 15 =", result(15))
# result = func_compute(4)
# print("Quadruple the number of 15 =", result(15))
# result = func_compute(5)
# print("Quintuple the number 15 =", result(15))

#======================================================================

# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list :")
# print(list)
# list.sort(key = lambda x: x[1])
# print("\nSorted:")
# print(list)
#======================================================================


# 6. Write a Python program to square and cube every number in 
# a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Original list: {list_nums}")
# square_nums = list(map(lambda x: x ** 2, list_nums))
# print (f"Square nums: {square_nums}")
# cube_nums = list(map(lambda x: x ** 3, list_nums))
# print(f"Cube nums: {cube_nums}")
#======================================================================

# 7. Write a Python program to find if a given string starts with a given 
# character using Lambda.
# Sample Output:
# True
# False

# word = "ISTAM"
# true_func = lambda word: True if word.startswith('I') else False
# false_func = lambda word: True if word.startswith('P') else False
# print(true_func(word))
# print(false_func(word))



# f1 = 0
# f2 = 1
# n = 10
# print(f1, f2, end = " ")
# while n > 1:
#     f1,f2 = f2, f1+f2
#     print(f2, end=" ")
#     n -= 1




# f1 = 0
# f2 = 1
# n = 10
# print(f1, f2, end = " ")
# for i in range(2, n):
#     f1,f2 = f2, f1+f2
#     print(f2, end=" ")



# f1 = 0
# f2 = 1
# n = 100
# print(f1, f2, end = " ")
# while f2 <n:
#     f1,f2 = f2, f1+f2
#     print(f2, end=' ')

















