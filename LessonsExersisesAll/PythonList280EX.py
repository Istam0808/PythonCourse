##PYTHON ##LIST ##EXERSISES
# ================================================================

# 1. Write a Python program to sum all the items in a list.
        #RU: 1. Напишите программу на Python для суммирования всех элементов списка.

# a = [1,2,3,4,5,6,7,8,9,10]
# c = 0
# for i in a:
#     c += i
# print (c)
    
# or

# a = [1,2,3,4,5,6,7,8,9,10]
# print(sum(a))
# ================================================================

# 2. Write a Python program to multiply all the items in a list.
        #RU: 2. Напишите программу на Python для умножения всех элементов списка.

# a = [1,2,3,4]
# b = 1
# for items in a:
#     b *= items
# print(b)   
# ================================================================

# 3. Write a Python program to get the largest number from a list.
        # RU: 3.Напишите программу на Python, чтобы получить наибольшее число из списка.

# a = [1,2,3,4,5]
# largest = a[0]
# for items in a:
#     if items > largest:
#         largest = items  
# print(largest)

#or

# a = [1,2,3,4,5]
# print(max(a))
# ================================================================

# 4. Write a Python program to get the smallest number from a list.
        # RU: 4. Напишите программу на Python, чтобы получить наименьшее число из списка.

# a = [1,2,3,4,5]
# smallest = a[1]
# for items in a:
#     if items < smallest:
#         smallest = items  
# print(smallest)

#or

# a = [1,2,3,4,5]
# print(min(a))
# ================================================================

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
        # RU: 5. Напишите программу на Python для подсчета количества строк из заданного списка строк. 
        #         Длина строки составляет 2 или более, а первый и последний символы совпадают.
        #         Список образцов: ['abc', 'xyz', 'aba', '1221']
        #         Ожидаемый результат: 2      

# a = ['istam', 'shaxa', 'av', 'aba']
# for i in a:
#     if len(i) >= 2:
#         if i == i[::-1]:
#             print(a.index(i))
    
#or with function (def)

# def count_strings(strings):
#     for i in strings:
#         if len(i) >= 2 and i[0] == i[-1]:
#             return strings.index(i)
# print(count_strings(['abc', 'xyz','qwert', '1221', 'aba']))
# ================================================================

# 6. Write a Python program to get a list, sorted in increasing order by the last element in 
# each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
        # RU: 6. Напишите программу на Python, чтобы получить список, отсортированный в порядке
        #         возрастания по последнему элементу в каждом кортеже из заданного списка непустых кортежей.
        #         Список образцов: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
        #         Ожидаемый результат: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
                         

# tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_tuples = sorted(tuples, key=lambda у: у[-1])
# print(sorted_tuples)
# ================================================================

# 7. Write a Python program to remove duplicates from a list.
        # RU: 7. Напишите программу на Python для удаления дубликатов из списка.

# a = ['a','b','c','a']
# print(sorted(set(a)))

#or

# a = [10,20,30,20,10,50,60,40,80,50,40]
# dup_i = set()
# uniq_i = []
# for x in a:
#     if x not in dup_i:
#         uniq_i.append(x)
#         dup_i.add(x)
# print(sorted(dup_i))
# ================================================================





























# ================================================================
