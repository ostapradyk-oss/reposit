# Example 1


class Human:
    height=170
    satiety=50

class Student(Human):
    satiety=0


class Worker(Human):
    satiety=100

Ostap=Student()
Viktor=Worker()
print(Ostap.satiety)
print(Viktor.satiety)
print(Ostap.height)
print(Viktor.height)


# Example 2




