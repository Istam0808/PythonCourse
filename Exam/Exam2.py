#FIRST TEST /// https://proglib.io/tests/test-na-znanie-yazyka-python
#SECOND TEST /// https://itproger.com/test/python


# EXAM EXERCISES

# 1. Create a function that finds n number of prime numbers.
# RU: Создайте функцию, которая находит n количество простых чисел.

# 2. Create a function that counts how much time that
# function takes to execute.
# RU: Создайте функцию, которая подсчитывает, сколько
# времени занимает выполнение этой функции.

# 3. Create a class that takes this function as a method
# and returns the execution time. Then, create an object
# and call the method.
# RU:   Создайте класс, который принимает эту функцию как метод.
# и возвращает время выполнения. Затем создайте объект
# и вызовем метод.

import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"the f:{func.__name__} take {round(total_time, 5)} seconds")
        return result
    return wrapper


@calc_time
def prime_nums(n):
    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
        num += 1
    return prime_numbers


@calc_time
def calculate_time(function, *args):
    result = function(*args)
    return result


nums_primes_before = 10000
print(prime_nums(nums_primes_before))

result = calculate_time(prime_nums, nums_primes_before)


class Timer:
    def __init__(self, func):
        self.func = func

    def f(self, *args):
        start_time = time.time()
        result = self.func(*args)
        end_time = time.time()
        finish_time = end_time - start_time
        return result, finish_time


timer = Timer(prime_nums)
result, execution_time = timer.f(nums_primes_before)
print(round(execution_time, 5))
