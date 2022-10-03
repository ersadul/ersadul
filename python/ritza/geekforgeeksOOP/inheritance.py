# # Inheritance in Python
# class Person(object):
    
#     def __init__(self, name, id='0'):
#         self.name = name 
#         self.id = id
    
#     # check if this person is an employee
#     def display(self):
#         print(self.name, self.id)
    
#     # to get name
#     def get_name(self):
#         return self.name
    
#     # check if this person is an employee or not
#     def is_employee(self):
#         return False
# driver code
# emp = Person('Satan', 666)
# emp.display()


# Creating a Child Class
# class Emp(Person):

#     def print(self):
#         print('emp class called')

# emp_details = Emp('Mephis', 69)
# emp_details.display()
# emp_details.print()


# Example of Inheritance in Python 
# class Person(object):
    
#     def __init__(self, name):
#         self.name = name 
    
#     # to get name
#     def get_name(self):
#         return self.name
    
#     # check if this person is an employee or not
#     def is_employee(self):
#         return False

# class Employee(Person):

#     # Here we return true
#     def is_employee(self):
#         return True
# # driver code
# emp = Person('Amon')
# print(emp.get_name(), emp.is_employee())
# emp = Employee('Hel')
# print(emp.get_name(), emp.is_employee())


# Subclassing (Calling constructor of parent class)
# parent class
# class Person(object):
#     # constructor
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number
    
#     def display(self):
#         print(self.name)        
#         print(self.id_number)

# # child class
# class Employee(Person):
#     def __init__(self, name, id_number, salary, post):
#         self.salary = salary
#         self.post = post

#         #invoking the init of the parent class
#         Person.__init__(self, name, id_number)

# a = Employee('Lucifer', 6969, 0, 'Earth')
# a.display()


# # Multiple inheritances
# class Base1(object):
# 	def __init__(self):
# 		self.str1 = "Geek1"
# 		print("Base1")

# class Base2(object):
# 	def __init__(self):
# 		self.str2 = "Geek2"
# 		print("Base2")

# class Derived(Base1, Base2):
# 	def __init__(self):

# 		# Calling constructors of Base1
# 		# and Base2 classes
# 		Base1.__init__(self)
# 		Base2.__init__(self)
# 		print("Derived")

# 	def printStrs(self):
# 		print(self.str1, self.str2)
# ob = Derived()
# ob.printStrs()


# # Private members of the parent class 
# class C:
#     def __init__(self):
#         self.c = 21
#         # d is private instance var
#         self.__d = 42

# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)

# obj1 = D()
# # produce an error as d is private instance var
# print(obj1.d)


# # note:
# source: https://www.geeksforgeeks.org/types-of-inheritance-python/
# Types of Inheritance in Python
# - Single Inheritance
# - Multiple Inheritance
# - Multilevel Inheritance
# - Hierarchical Inheritance
# - Hybrid Inheritance