# Chapter 20: Dictionaries
# 22.1. MyTime
# class MyTime:

#     def __init__(self, hrs=0, mins=0, secs=0):
#         """Create a MyTime object initialized to hrs, mins, and secs"""
#         self.hours = hrs
#         self.minutes = mins
#         self.seconds = secs

#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'

# 22.2. Pure functions
# def add_time(t1, t2):
#     h = t1.hours + t2.hours
#     m = t1.minutes + t2.minutes
#     s = t1.seconds + t2.seconds

#     if s >= 60:
#         s -= 60
#         m +=1
#     if m >= 60:
#         m -= 60
#         h +=1
#     return MyTime(h, m, s)

# time1 = MyTime(11, 59, 30)
# print(time1)

# current_time = MyTime(9, 14, 30)
# bread_time = MyTime(3, 35, 0)
# done_time = add_time(current_time, bread_time)
# print(done_time)

# 22.3. Modifiers
def increment(t, seconds):
    t.seconds += seconds
    # # use if clause, if seconds < 60
    # if t.seconds >= 60:
    #     t.seconds -= 60
    #     t.minutes += 1
    # if t.minutes >= 60:
    #     t.minutes -= 60
    #     t.hours += 1

    # use while clause, if seconds > 60
    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1
    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1

# 22.4. Converting increment to a method
# class MyTime:

#     def __init__(self, hrs=0, mins=0, secs=0):
#         """Create a MyTime object initialized to hrs, mins, and secs"""
#         self.hours = hrs
#         self.minutes = mins
#         self.seconds = secs

#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'
    
#     def increment(self, seconds):
#         self.seconds += seconds

#         while self.seconds >= 60:
#             self.seconds -= 60
#             self.minutes += 1

#         while self.minutes >= 60:
#             self.minutes -= 60
#             self.hours += 1

# current_time = MyTime(9, 14, 30)
# print(current_time)
# current_time.increment(500)
# print(current_time)

# 22.5. An “Aha!” insight
# class MyTime:

#     def __init__(self, hrs=0, mins=0, secs=0):
#         """Create a MyTime object initialized to hrs, mins, and secs.
#         and normalize the atribute"""
#         total_secs = hrs * 3600 + mins * 60 + secs 
#         self.hours = total_secs // 3600
#         leftover_secs = total_secs % 3600
#         self.minutes = leftover_secs // 60
#         self.seconds = leftover_secs % 60

#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'
    
#     def to_seconds(self):
#         """Return the number of seconds of this instance"""
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

# def add_time(t1, t2):
#     secs = t1.to_seconds() + t2.to_seconds()
#     return MyTime(0, 0, secs)

# current_time = MyTime(9, 14, 30)
# bread_time = MyTime(3, 35, 0)
# done_time = add_time(current_time, bread_time)
# print(done_time)


# 22.6. Generalization

# 22.7. Another example
# class MyTime:

#     def __init__(self, hrs=0, mins=0, secs=0):
#         """Create a MyTime object initialized to hrs, mins, and secs.
#         and normalize the atribute"""
#         total_secs = hrs * 3600 + mins * 60 + secs 
#         self.hours = total_secs // 3600
#         leftover_secs = total_secs % 3600
#         self.minutes = leftover_secs // 60
#         self.seconds = leftover_secs % 60

#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'
    
#     def to_seconds(self):
#         """Return the number of seconds of this instance"""
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

    # we dont need to do this way, because we do Generalization into the lower level
    # def after(self, time2):
    #     """ Return True if I am strictly greater than time2 """
    #     if self.hours > time2.hours:
    #         return True
    #     if self.hours < time2.hours:
    #         return False

    #     if self.minutes > time2.minutes:
    #         return True
    #     if self.minutes < time2.minutes:
    #         return False
    #     if self.seconds > time2.seconds:
    #         return True

    #     return False

    # we just need to do this way, more simplified way
    # def after(self, time2):
    #     """ Return True if I am strictly greater than time2 """
    #     return self.to_seconds() > time2.to_seconds()


# 22.8. Operator overloading
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, and secs.
        and normalize the atribute"""
        total_secs = hrs * 3600 + mins * 60 + secs 
        self.hours = total_secs // 3600
        leftover_secs = total_secs % 3600
        self.minutes = leftover_secs // 60
        self.seconds = leftover_secs % 60

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    
    def to_seconds(self):
        """Return the number of seconds of this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = t1 + t2
# print(t3)
# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = t1 - t2
# print(t3)

class Point:
    """Create a point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)
    
    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

# p1 = Point(3, 4)
# p2 = Point(5, 7)
# print(p1 * p2)
# print(2 * p2)


# 22.9. Polymorphism
# def multadd(x, y, z):
#     return x * y + z

# print(multadd(3, 2, 1))
# p1 = Point(3, 4)
# p2 = Point(5, 7)
# print(multadd(2, p1, p2))
# print(multadd(p1, p2, 1))

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))

my_list = [1, 2, 3, 4]
front_and_back(my_list)

p = Point(3, 4)
front_and_back(p)