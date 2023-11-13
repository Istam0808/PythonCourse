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

lesson = "Decorators & Wrappers"
# Decorators are functions that take another function as an argument, add some kind of functionality,
# and then return another function. All of this without altering the source code of the original
# function that we passed in. In Python, functions are first-class objects, which means that we can
# pass them as arguments to other functions. We can also return them as the values from other functions.
# This is the basis of decorators.

####################################################################################
####################################################################################
####################################################################################
# BASIC DECORATOR


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Wrapper executed this before {}".format(
#             original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def original_function():
#     print("Original function ran")

####################################################################################
# defining a decorator


# def hello_decorator(func):

#     # inner1 is a Wrapper function in
#     # which the argument is called

#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")
#         # calling the actual function now
#         # inside the wrapper function.
#         result = func()
#         print("This is after function execution")
#         return result

#     return inner1


# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")


# # # passing 'function_to_be_used' inside the
# # # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)


# # calling the function
# function_to_be_used()


####################################################################################
####################################################################################
####################################################################################
# Practical example 1
# find out the execution time of a function using a decorator.

# decorator to calculate duration
# taken by any function.
# def calculate_time(func):

#     # added arguments inside the inner1,
#     # if function takes any arguments,
#     # can be added like this.
#     def inner1(*args, **kwargs):

#         # storing time before function execution
#         begin = time.time()

#         func(*args, **kwargs)

#         # storing time after function execution
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)

#     return inner1


# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):

#     # sleep 2 seconds because it takes very less time
#     # so that you can see the actual difference
#     time.sleep(2)
#     print(math.factorial(num))


# # calling the function.
# factorial(10)

####################################################################################
####################################################################################
####################################################################################
# RETURN A VALUE

# def hello_decorator(func):
#     def inner1(*args, **kwargs):

#         print("before Execution")

#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")

#         # returning the value to the original frame
#         return returned_value

#     return inner1


# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b


# a, b = 1, 2

# # getting the value through return of the function
# sum = sum_two_numbers(a, b)
# print("Sum =", sum)
####################################################################################
####################################################################################
####################################################################################
# MEMOIZATION
# Factorial program with memoization using decorators.

# A decorator function for function 'f' passed
# as parameter
# memory = {}


# def memoize_factorial(f):

#     # This inner function has access to memory
#     # and 'f'
#     def inner(num):
#         if num not in memory:
#             memory[num] = f(num)
#             print('result saved in memory')
#         else:
#             print('returning result from saved memory')
#         return memory[num]

#     return inner


# @memoize_factorial
# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num-1)


# print(facto(5))
# print(facto(5))  # directly coming from saved memory
# print(memory)
