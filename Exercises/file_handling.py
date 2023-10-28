# 1. Create and write to a file with names and read the file and print the names and the number of times they appear in the file.
# RU: Создайте и запишите в файл имена, прочитайте файл и напечатайте имена и количество раз, которое они встречаются в файле.
def read_names():
    file = open("nameslist.txt", "r")
    names = file.read().split("\n")
    names.sort()
    names_set_list = list(set(names))
    names_set_list.sort(key=lambda x: names.count(x))
    for name in names_set_list:
        print(name + ": " + str(names.count(name)))


def create_names(names):
    file = open("nameslist.txt", "w")
    for name in names:
        file.write(name + "\n")
    file.close()


names = [
    "Oliver", "George", "Harry", "Jack", "Jacob", "Noah",
    "Charlie", "Muhammad", "Thomas", "Oscar", "William",
    "James", "Leo", "Alfie", "Henry", "Archie", "Ethan",
    "Charlie", "Muhammad", "Thomas", "Oscar", "William",
    "Joseph", "Freddie", "Samuel", "Alexander", "Logan"
]

create_names(names)
read_names()

# ======================================================================================================================
# ======================================================================================================================
# 2. Create a file with numbers and read the file and print the sum of all numbers.
# RU: Создайте файл с числами, прочитайте файл и напечатайте сумму всех чисел.


def read_numbers_and_sum():
    file = open("numbers.txt", "r")
    numbers = file.read().split("\n")
    print("numbers: ", numbers)
    numbers = [int(n.strip()) for n in numbers if n]
    print(sum(numbers))


def create_numbers():
    numbers = [int(n.strip())
               for n in input("Enter numbers: ").split(',') if n.strip().isnumeric()]
    file = open("numbers.txt", "w")
    for number in numbers:
        file.write(str(number) + "\n")
    file.close()


create_numbers()
read_numbers_and_sum()


# ======================================================================================================================
# ======================================================================================================================
