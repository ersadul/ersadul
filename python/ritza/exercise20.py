# 22.11. Exercises
from unit_tester import test

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
    
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()
    
    # 3. operator overloading method >, related to after method(above)
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()
    
    # 1. &  2.
    def between(self, t1, t2):
        if t1.to_seconds() <= self.to_seconds() \
            and self.to_seconds() < t2.to_seconds():
            return True
        else:
            return False
    
    # 4. &  5.
    def __iadd__(self, other):
        if (self.seconds + other) <= self.seconds:
            raise ValueError("you mustn't subtract below the base time")
        self.seconds += other
        
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        return self

# 1. Write a Boolean function between that takes two MyTime objects, t1 and t2, as arguments, and
# returns True if the invoking object falls between the two times. Assume t1 <= t2, and make the
# test closed at the lower bound and open at the upper bound, i.e. return True if t1 <= obj < t2.
# 2. Turn the above function into a method in the MyTime class
# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = MyTime(2, 0, 0)
# print(t3.between(t1, t2))

# 3. Overload the necessary operator(s) so that instead of having to write :
# if t1.after(t2): …
# we can use the more convenient :
# if t1 > t2: …
# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# if t1 > t2:
#     print('t1 is greater than t2')
# else:
#     print('t1 is not greater than t2')

# 4. Rewrite increment as a method that uses our “Aha” insight
# 5. Create some test cases for the increment method. Consider specifically the case where the number
# of seconds to add to the time is negative. Fix up increment so that it handles this case if it does not do
# so already. (You may assume that you will never subtract more seconds than are in the time object.)
t1 = MyTime(1, 15, 42)
print(hex(id(t1)), t1)
t1 += 10
print(hex(id(t1)), t1)


