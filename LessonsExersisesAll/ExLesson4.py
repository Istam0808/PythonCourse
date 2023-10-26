#HOMEWORK


#1 LAST LETTER BEFORE

# def last_l_before(string, stop=1):
#     if stop == 0:
#         return
#     elif len(string) == 1:
#         print(string)
#     else:
#         print(string)
#         last_l_before(string[-1] + string[:-1], stop=stop-1)
# last_l_before("Hello world", stop=len("Hello world")+1)


#2 PYRAMID WITH RECURSION 

# def pyramida(n, current=1):
#     if current >= n:
#         return
#     else:
#         print(' ' * (n - current) + '*' * (2 * current - 1))
#         pyramida(n, current + 1)

# n = int(input('>>>: '))
# pyramida(n)


# x = lambda string1, string2: string1 + string2
# print(x("Istam", "jamshed"))



