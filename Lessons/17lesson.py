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

# defining a decorator
# def hello_decorator(func):                                              #2 STEP
 
#     # inner1 is a Wrapper function in 
#     # which the argument is called
     
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():                                                       #3 STEP
#         print("Hello, this is before function execution")
 
#         # calling the actual function now
#         # inside the wrapper function.
#         func()
 
#         print("This is after function execution")
#     return inner1                                                       #4 STEP
 
 
# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")
 
 
# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)              #1 STEP
 
 
# # calling the function
# function_to_be_used()                                                   #5 STEP

