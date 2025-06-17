# # # # class Animal:
# # # #     def make_sound(self):
# # # #         return "издает звук"
# # # #
# # # #
# # # # class FlyableAnimal:
# # # #     def move(self):
# # # #         return "Летит"
# # # #
# # # # class SwimableAnimal:
# # # #     def move(self):
# # # #         return "Плавает"
# # # #
# # # # class Duck(Animal, FlyableAnimal, SwimableAnimal):
# # # #     pass
# # # #
# # # # donald = Duck()
# # # # print(donald.move())
# # #
# # # class A:
# # #     def test_method(self):
# # #         return 'Class A'
# # #
# # # class B(A):
# # #     def test_method(self):
# # #         return 'Class B'
# # #
# # # class C(A):
# # #     def test_method(self):
# # #         return 'Class C'
# # #
# # # class D(B,C):
# # #     def test_method(self):
# # #         return 'Class D'
# #
# # class Math:
# #
# #     # Атрибут класса
# #     sum = 123
# #
# #     #Атрибут объекта класса|экземпляр класса
# #     def __init__(self, test):
# #         self.test = test
# #
# #     @staticmethod
# #     def add(a,b):
# #         return a+b
# #
# #     @classmethod
# #     def get_sum(cls):
# #         return cls.sum
# #
# #     @
# # # print(Math.sum)
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def get_radius(self):
#         return self.__radius
#
#     @property
#     def get_area(self):
#         return 3.14 * self.__radius ** 2
#
# circle_1 = Circle(5)
# print(circle_1.get_radius)

def my_decorator(func):
    def wrapper():
        print('Перед выполнением функции ')
        func()
        print('После выполнения функции')
        print('============================')
    return wrapper
@my_decorator
def hello():
    print('hello world')
@my_decorator
def main():
    print('main')
# hello()
# main()

#Декораторы с параметрами|аргументы

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(5)
def hello():
    print('hello!!!')

# hello()
def class_decorator(cls):
     class NewClass(cls):
         def new_method(self):
             return 'new method'
     return NewClass
@class_decorator
class MyClass():
     def old_method(self):
         return 'old method'

obj = MyClass()
print(obj)

