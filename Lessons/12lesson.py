# DICT COMPREHENSION

#First Exersise

# x1 = {'a': 1, 'b': 2}
# x2 = {'c': 3, 'd': 4}
# x3 = {'e': 5, 'f': 6}
# def concatenate_dict(*args):
#     return {key:value for dict in args for key,value in dict.items()}
# print(concatenate_dict(x1, x2, x3))

#Second Exersise

# def check_key(dict,key):
#     return "HAS" if key in dict else "NOT"
# x1 = {'a': 1, 'b': 2}
# print(check_key(x1,'b'))

#Third Exersise

# def iterate_over_dict(dict):
#     # for k,v in dict.items():
#     #     print(k,v)
#     {"":print(k,v) for k,v in dict.items()}
#
# iterate_over_dict({
#     'name' : 'John',
#     'age' : 26,
#     'addres' : 'Norway'
#     })

#Fourth Exersise 

# mdict = {"a": "1", "b": 2, "c": 3}
# num = sum(v if isinstance(v, int) else int(v) for v in mdict.values())
# # for v in mdict.values():
# #     if type(v) == int:
# #         num += v
# #     elif v.isnumeric():
# #         num += int(v)
# print("Сумма :", num)




