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

# 8. Write a Python program to check if a list is empty or not.
        #RU : 8. Напишите программу на Python, проверяющую, пуст ли список или нет

# l = [13]
# if not l:
#     print("Список пуст")
# else:
#     print("список полный")
# ================================================================

# 9. Write a Python program to clone or copy a list.
        # RU: 9. Write a Python program to clone or copy a list.

# list1 = ['a','b','c']
# copy_list = list(list1.copy())
# copy_list.insert(0,'s')

# print(f"original_list: {list1}")
# print(f"copy_list: {copy_list}")
# ================================================================

# 10. Write a Python program to find the list 
# of words that are longer than n from a given list of words.
        #RU: 10. Напишите программу на Python, 
        # чтобы найти список слов длиной более n из заданного списка слов.

# def find_list(n,lis:list):
#     for i in lis:
#         if len(i) == n:
#             print(i)
# find_list(5, ['istam','rusik',"shax"])
# ================================================================

# 11. Write a Python function that takes two lists and
# returns True if they have at least one common member.
        # RU: 11. Напишите функцию Python, которая принимает два списка и возвращает True, 
        #     если у них есть хотя бы один общий член.

# def common_members(list1,list2):
#     result = ''
#     for i in list1:
#         for x in list2:
#             if i == x:
#                 result = 'Есть одинаковый'
#                 return result
# print(common_members([1,2,3,4,5], [5,6,7,8,9]))
# print(common_members([1,2,3,4,5], [6,7,8,9]))
# ================================================================

# 12. Write a Python program to print a specified 
# list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
                # RU:12. Напишите программу на Python для печати указанного списка после удаления 
                #         0-го, 4-го и 5-го элементов.
                #         Список образцов: ['Красный', 'Зеленый', 'Белый', 'Черный', 'Розовый', 'Желтый'] 
                #         Ожидаемый результат: ['Зеленый', 'Белый', 'Черный']
                                                       
# a = ['Красный', 'Зеленый', 'Белый', 'Черный', 'Розовый', 'Желтый']
# print(f"original list: {a}")
# b = a.copy()
# b.remove(a[0])
# b.remove(a[4])
# b.remove(a[5])
# print(f"copy list: {b}") 

#or with LIST COMPREHENSION

# a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(f"before: {a}")
# a = [x for (i,x) in enumerate(a) if i not in (0,4,5)]
# print(f"after: {a}")
# ================================================================

# 13. Напишите программу на Python для печати чисел указанного
#  списка после удаления из него четных чисел.

# a = [1,2,3,4,5,6,7,8,9,10]
# a = [i for i in a if i %2 != 0]
# print(a)
# ================================================================

# 15. Напишите программу на Python для перетасовки и печати указанного списка.

# from random import shuffle
# a = ["apple", "orange", "istam", "rustam", "shaxa"]
# print(f"original {a}")
# shuffle(a)
# print(f"shuffle {a}")
# ================================================================
