# Python Classes and Objects
# www.geeksforgeeks.org

# class Dog:
#     # a simple class attribute
#     attr1 = 'mammal'
#     attr2 = 'dog'

#     # a sample method
#     def fun(self):
#         print("I'am a", self.attr1)
#         print("I'am a", self.attr2)

# # object instantiation
# rodger = Dog()

# # accessing class attribute and method through object
# print(rodger.attr1)
# rodger.fun()


# Class and Instance Variables
# class Dog:
#     #class variable
#     animal = 'dog'

#     # init method or constructor
#     def __init__(self, breed='', color=''):
#         # instance variable
#         self.breed = breed
#         self.color = color
    
#     # adds an instance var
#     def set_color(self, color):
#         self.color = color
    
#     # retrieves instance variable
#     def get_color(self):
#         return self.color
    

# rodger = Dog('pug', 'brown')
# buzo = Dog('bulldog', 'black')
# print('Rodger details:')
# print('Rodger is a', rodger.animal)
# print('Breed: ', rodger.breed)
# print('Color: ', rodger.color)
 
# print('\nBuzo details:')
# print('Buzo is a', buzo.animal)
# print('Breed: ', buzo.breed)
# print('Color: ', buzo.color)

# # Class variables can be accessed using class
# # name also
# print("\nAccessing class variable using class name")
# print(Dog.animal)


# Defining instance variables using the normal method
# rodger = Dog('pug')
# rodger.set_color('brown')
# print(rodger.get_color())



# # Constructors in Python
# class GeekforGeeks:
 
#     # default constructor
#     def __init__(self):
#         self.geek = "GeekforGeeks"
 
#     # a method for printing data members
#     def print_Geek(self):
#         print(self.geek)
 
 
# # creating object of the class
# obj = GeekforGeeks()
# # calling the instance method using the object obj
# obj.print_Geek()


# Example of the parameterized constructor : 
# class Addition:
#     first = 0
#     second = 0
#     answer = 0

#     # parameterized constructor
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s

#     def display(self):
#         print('First number =', self.first)
#         print('Second number =', self.second)
#         print('Addition of two number =', self.answer)

#     def calculate(self):
#         self.answer = self.first + self.second

# # creating object of the class
# # this will invoke parameterized constructor
# obj = Addition(1000, 2000)
# # perform Addition
# obj.calculate()
# # display result
# obj.display()



# Destructors in Python
# class Employee:
    
#     def __init__(self):
#         print('Employee created')
    
#     def __del__(self):
#         print('Destructor called, employee deleted')

# obj = Employee()
# del obj
