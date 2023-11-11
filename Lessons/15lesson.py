# lesson = "Class  &&  OOP"
# _1 = 'Abstract and Inheritance'

# from abc import ABC, abstractmethod


# class AnimalAbstractClass(ABC):


#     def __init__(self, name,*args):
#         print("Class obj has been crated")
#         self.name = name
        

#     def __str__(self):
#         return f"class {self.name}"

    
#     @abstractmethod
#     def get_info(self):
#         raise NotImplementedError



# class Tiger(AnimalAbstractClass):
#     def __init__(self, name:str, age:int, speed:int) -> None:
#         super().__init__(name)
#         self.age = age
#         self.speed = speed

#     def get_info(self):
#         return f"{self.name} is {self.age} years old and can run {self.speed}"

# tiger1 = Tiger("White tiger", 10, 25)
# print(tiger1)
# print(tiger1.get_info())

# ====================================================================================
# from abc import ABC, abstractmethod


# class AbcBook(ABC):
#     def __init__(self, name, page):
#         self.name = name
#         self.page = page


# class Paper_Book(AbcBook):
#     def __init__(self, name, page):
#         super().__init__(name, page)

    
#     def get_description(self):
#         return f"In {self.name} {self.page} pages"


# Book = Paper_Book("PaperBook", "100")
# print(Book.get_description())


# class Ebook(AbcBook):
#     def __init__(self, ip, bbooks):
#         super().__init__("Ebook", ip)
#         self.bbooks = bbooks
#         self.ip = ip

#     def get_description(self):
#         return f"ip {self.bbooks} is {self.ip }"


# EEBook = Ebook("192.168.0.132", "Ebook")
# print(EEBook.get_description())

# class Online_Book(AbcBook):
#     def __init__(self, pagess, ipps, pigass):
#         super().__init__("Online_Book", ipps)
#         self.pagess = pagess
#         self.ipps = ipps
#         self.pigass = pigass

#     def get_description(self):
#         return f"ip {self.pagess} is {self.ipps }\n{self.pagess} pages = {self.pigass} "


# OnBook = Online_Book("Online_Book", "192.168.0.132", 100)
# print(OnBook.get_description())

# ====================================================================================

# from abc import ABC, abstractmethod

# class Paper_Book(ABC):
#     def __init__(self, name, page):
#         self.name = name
#         self.page = page

#     @abstractmethod
#     def get_description(self):
#         pass


# class Electronic_Book(Paper_Book):
#     def __init__(self, name, paper, ip):
#         super().__init__(name,paper)
#         self.ip = ip
#         self.paper = paper
#     def get_description(self):
#         return f"In {self.name} is {self.paper}, and ip is {self.ip} "
# el_books = Electronic_Book("El_Book", 100, "12432.234324.234")
# print(el_books.get_description())


# class Online_Book(Electronic_Book):
#     def __init__(self, name, paper):
#         self.paper = paper
#         self.name = name
#     def get_description(self):
#         return f"In {self.name} is {self.paper} paper"
# onl_books = Online_Book("Olivers_book", 20)
# print(onl_books.get_description())




# ====================================================================================

# Abstract
# Inheritance

# this == self

# class User:
#     def __init__(self, name):
#         print(f"User {name} is created")
#         self.name = name

# user1 = User("John")
# print(user1)
# print(user1.name)


# __init__  => is a constructor method which is used to initialize the attributes of a class
# it is called automatically when an object is created

#############################################################################################
################ Abstraction

# "abc" here stands for abstract base class. It is first imported and then used as 
# a parent class for some class that becomes an abstract class. Its simplest implementation 
# can be done as below.


# from abc import ABC, abstractmethod
# class AbcAnimal(ABC):
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food

#     @abstractmethod
#     def get_description(self):
#         pass
#         # raise NotImplementedError


# class Pets(AbcAnimal):
#     def __init__(self, name, food, speed):
#         super().__init__(name, food)
#         self.speed = speed

#     def get_description(self):
#         return f"{self.name} eats {self.food}"


# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_description())



# abs module is used to create abstract classes
# it is helpful when we want to create a class that will be used as a base class
# abstractmethod is used to declare abstract methods which will be implemented by the child classes
# is it used to ensure that the child classes will have the same method as the parent class
# and returns an error if the child class does not have the same method as the parent class
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.

#############################################################################################
################ Inheritence

# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def test(self):
#         print("Hello world")

# class Child(Parent, ABC):
# #     Inherited members from parent class
# #     Additional members of the child class
#     def __init__(self, name, age):
#         super().__init__(name)  # => calls the parent class constructor
#         self.age = age

#     def test(self):
#         print("Hello world from child")

#     def __repr__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for debugging and logging.
#         '''
#         return f"{self.name} is {self.age} years old"

#     def __str__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for the end user.
#         '''
#         return f"{self.name} is {self.age} years old"


# child = Child("John", 20)
# print(child)
# print(child.test())
