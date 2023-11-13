# def decorator_function(org_func):
#     def wrapper_function(*args, **kwargs):
#         print(f"Wrapper execude this before {org_func.__name__}")
#         return org_func(*args,**kwargs)
#     return wrapper_function


# @decorator_function
# def original_function(*args):
#     print("Original function ran")

# x = [1,2,3,4,5]
# original_function(x)

#========================================================================================

# import math
# import time

# def calculate_time(func):
#     def inner1(*args,**kwargs):
#         begin = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
#     return inner1


# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(5)

#========================================================================================


# memory = {}

# def memoize_factorial(f):
#     def inner(num):
#         if num not in memory:
#             memory[num] = f(num)
#             print('result saved in memory')
#         else:
#             print('FROM SAVED MEMORY: ', memory[num])
#         return memory[num]
#     return inner


# @memoize_factorial
# def facto(num):
#     if num ==1:
#         return 1
#     else:
#         return num*facto(num-1)

# print(facto(5))    
# print(facto(5))    
# print(facto(3))
# print(memory)    

#========================================================================================

def check_input(fn):
    def wrapper(*args, **kwargs):
        for i in args:
            if not i.isalnum():
                raise Exception("Invalid value")
        return fn(*args,**kwargs)