# # Encapsulation in Python
# Protected member
# class Base:
#     def __init__(self):
#         #protected member
#         self._a = 2

# class Derived(Base):
#     def __init__(self):
#         # calling constructor of Base class
#         Base.__init__(self)
#         print('call protected member of base class:', self._a)

#         # modify the protected var 
#         self._a = 3
#         print('call protected member of base class:', self._a)

# obj1 = Derived()
# obj2 = Base()
# # Calling protected member
# # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)


# Private members
# class Base:
#     def __init__(self):
#         self.a = 'Geeks'
#         self.__c = 'forGeeks'

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('call private member of class Base:', self.__c)

# obj1 = Base()
# print(obj1.a)

# obj2 = Derived()

