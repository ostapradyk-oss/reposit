# Example 1


# class Human:
#     height=170
#     satiety=50
#
# class Student(Human):
#     satiety=0
#
#
# class Worker(Human):
#     satiety=100
#
# Ostap=Student()
# Viktor=Worker()
# print(Ostap.satiety)
# print(Viktor.satiety)
# print(Ostap.height)
# print(Viktor.height)


# Example 2

# class Didus:
#     height=190
#     satiety=100
#     age=60
# class Batko(Didus):
#     age=40
# class Child(Batko):
#     height=50
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)


# Example 3


# class Hello_World:
#     hello='hello'
#     _hello='_hello'
#     __hello='__hello'
#
#     def __init__(self):
#         self.world='World'
#         self._world='_World'
#         self.__world=('__World')
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
#
# class hi(Hello_World):
#     def hiprint(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# helloworld=Hello_World()
# hi=hi()
# Hello_World.printer()
# hi.hiprint()




# Example 4


class Compute:
    def calculate(self):
        print('calculating... idk bru')

class Display:
    def display(self):
        print('I display the display on the display')


class Smartphone(Display, Compute):
    pass

phone=Smartphone()
phone.display()
phone.calculate()































