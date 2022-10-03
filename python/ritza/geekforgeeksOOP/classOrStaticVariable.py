# Class or Static Variables in Python
# class CSStudent:
#     stream = 'cse'
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# a = CSStudent('Geek', 1)
# b = CSStudent('Nerd', 2)

# print(a.stream)  # prints "cse"
# print(b.stream)  # prints "cse"
# print(a.name)    # prints "Geek"
# print(b.name)    # prints "Nerd"
# print(a.roll)    # prints "1"
# print(b.roll)    # prints "2"

# print(CSStudent.stream)
# # Now if we change the stream for just a it won't be changed for b
# a.stream = 'ece'
# print(a.stream)
# print(b.stream)
# # to change stream for all instance 
# CSStudent.stream = 'mech'
# print(a.stream)
# print(b.stream)


# Class method vs Static method in Python
# class method: It can modify a class state that would apply across all the instances of the class.
# static method: This method can’t access or modify the class state. 
# - A class method takes cls as the first parameter while a static method needs no specific parameters.
# - A class method can access or modify the class state while a static method can’t access or modify it.
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # a class method to create a Person object by birth year
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
    
    # a static method to check if a Person is adult or not
    @staticmethod
    def is_adult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.from_birth_year('mayank', 1996)
print(person1.age)
print(person2.age)
# print the result
print(Person.is_adult(22))

