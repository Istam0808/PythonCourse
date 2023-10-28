# 1. Factorial      =>   !5  =  5*4*3*2*1
# factorial(10)   =>   !10 =  10*9*8*7*6*5*4*3*2*1
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

# ==============
# 2. Fibonacci  =>   0, 1  =  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# fibbo(50)     =>   0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fibonacci(max, first=0, second=1):
    if first > max:
        return []
    else:
        return [first, *fibonacci(max, second, first+second)]


print(fibonacci(50))
# ==============
# 3. Piramid
# piramid(10)
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************


def piramid_recursion(n_times):
    if n_times == 1:
        return "*"
    else:
        return "*" * n_times + "\n" + piramid_recursion(n_times-1)
    # ===============
    # With loop
    # result = ""
    # for i in range(n_times):
    #     result += "*" * (i+1) + "\n"
    # return result


piramid_recursion(10)

# ====================================================================
# ! USE RECURSION


def rotate_string_recursively(string, remaining_str=""):
    if len(remaining_str) == 0:
        remaining_str = string

    new_str = string[-1] + string[:-1]
    if len(remaining_str) == 1:
        print(new_str)
        return

    print(string)
    return rotate_string_recursively(new_str, remaining_str[:-1])

# rotate_string_recursively("Hello world")
# >> Hello world
# >> dHello worl
# >> ldHello wor
# >> rldHello wo
# >> orldHello w
# >> worldHello
# >>  worldHello
# >> o worldHell
# >> lo worldHel
# >> llo worldHe
# >> ello WorldH
# >> Hello World
# ====================================================================
