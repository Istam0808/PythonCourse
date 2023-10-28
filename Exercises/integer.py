# 1. Reverse an integer.
# RU: Обратный порядок целого числа.
def reverse_integer(num):
    return str(num)[::-1]

# 2. Print the Fibonacci series using the recursive method.
# fibonacci(10)   =>   0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
# RU: Выведите ряд Фибоначчи с помощью рекурсивного метода.
def fibonacci(max, first:int=0, second:int=1):
    # ================================================================
    # FIRST METHOD----------------------------------------------------
    if max > first:
        return []
    return [first] + fibonacci(max, second, first + second)
    # ================================================================
    # SECOND METHOD---------------------------------------------------
    # List comprehension
    # return [first] + fibonacci(max, second, first + second) if max > first else []
    # ================================================================
    # THIRD METHOD----------------------------------------------------
    # if max <= 1:
    #     return max
    # else:
    #     return fibonacci(max-1) + fibonacci(max-2)
    
    

# 3. Return the Nth value from the Fibonacci sequence.
# fibonacci(10)   =>   0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...  => 34
# RU: Вернуть N-е значение из последовательности Фибоначчи.


# 4. Find an average number of given numbers of the list and return nearest integer
# from given list
# RU: Найти среднее число данного списка и вернуть ближайшее целое число
# из данного списка.
# INPUT:  [1, 10, 40, 35, 20, 30, 50, 60, 70]
# OUTPUT: 37.777...  =>  35  =>  index-3
# =================================================================================

# 5. Print stars downwards starting from n number
# RU: Распечатать звезды вниз, начиная с числа n
def print_stars(max):
    # for i in range(max):
    #     print('*' * (max - i))
    if max==0: 
        return
    print(max * '*')
    return print_stars(max-1)
print_stars(10)

# =================================================================================
# 6. Print stars (*) in the shape of a pyramid with N number of steps.
# pyramid(4) =>
#    *
#   ***
#  *****
# *******
# =================================================================================


# 5. Convert Celsius to Fahrenheit.
# RU: Преобразование Цельсия в Фаренгейт.