# 1. Write a Python program to create a decorator that logs the arguments and return value of a function.
# RU: Напишите программу на Python для создания декоратора, который регистрирует аргументы и возвращаемое значение функции.
def decorator_fn(fn):
    def wrapper(*args, **kwargs):
        print(
            f"Printing args before execution of original function {fn.__name__}")
        print(args)
        return fn(*args, **kwargs)
    return wrapper


@decorator_fn
def test_fn2(string):
    print("Inside the original function")
    return string


test_fn2("Test-Sentence")
# ###################################################################################
# ###################################################################################
# ###################################################################################

# 2. Write a Python program to create a decorator function to measure the execution time of a function.
# RU: Напишите программу на Python для создания декоратора функции для измерения времени выполнения функции.


def calculate_time_dec(fn):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper


@calculate_time_dec
def test_fn(string):
    print("Inside the original function")
    return string


test_fn("Test-Sentence")

# ###################################################################################
# ###################################################################################
# ###################################################################################

# 3. Create a decorator to check the input values of a function and
# raise an exception if the input values are not of the expected type.
# RU: Создайте декоратор для проверки входных значений функции и
# вызовите исключение, если входные значения не соответствуют ожидаемому типу.
# Expected types of input: int, string
# raise Exception("Invalid input type")


def check_input(fn):
    """is used to check if the given input is alpha-numerical"""
    def wrapper(*args, **kwargs):
        for item in args:
            if not item.isalnum():
                raise Exception("Invalid value")
        return fn(*args, **kwargs)
    return wrapper


@check_input
def get_text(string):
    print("Inside the original function")
    return string

# answer = input("Enter a alpha numeric value please: ")
# print(get_text(answer))


# ###################################################################################
# 4. Write a Python program that implements a decorator to retry a function
# 3 times in case of failure.
# RU: Напишите программу на Python, которая реализует декоратор для повторного
# вызова функции 3 раза в случае сбоя.
def retry(fn):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return fn(*args, **kwargs)
            except:
                print("Retrying...")
    return wrapper


@retry
def test_fn3(string):
    print("Inside the original function")
    raise Exception("Test exception")


# ###################################################################################
# 5. Write a Python program that implements a decorator that records time when
# the function has been called
def record_time(fn):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper


@record_time
def test_fn4(string):
    print("Inside the original function")
    return string

# ###################################################################################
# 6. Write a Python program that implements a decorator to handle exceptions raised
# by a function and provide a default response.


def handle_exception(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except:
            print("Exception handled")
            return "Default response"
    return wrapper


@handle_exception
def test_fn5(string):
    print("Inside the original function")
    raise Exception("Test exception")

# ###################################################################################
# 7. Write a Python program that implements a decorator to measure the memory usage of a function.


def measure_memory(fn):
    def wrapper(*args, **kwargs):
        import memory_profiler

        # install memory_profiler with pip install memory_profiler
        result = memory_profiler.memory_usage()
        # memory usage shows the memory usage of the current process in kilobytes
        return result
    return wrapper


@measure_memory
def test_fn6(string):
    print("Inside the original function")
    return string

# ###################################################################################


# 8. Write a Python program that implements a decorator to provide caching
# cache = {}


# def cache(fn):
    def wrapper(*args, **kwargs):
        cache[args] = fn(*args, **kwargs)
        return cache[args]
    return wrapper


# @cache
# def test_fn7(string):
    print("Inside the original function")
    return string
# ###################################################################################
