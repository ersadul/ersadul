# # 15.12. Exercises

# 1. Rewrite the distance function from the chapter titled Fruitful functions so that it takes two
# Points as parameters instead of four numbers.
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dxsquared = dx*dx + dy*dy
#     return dxsquared ** 0.5

# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def distance(p1, p2):
#         dx = p2x - p1.x 
#         dy = p2y - p1.y 
#         return ((dx * dx) + (dy * dy)) ** 0.5


# 2. Add a method reflect_x to Point which returns a new Point, one which is the reflection of the
# point
# about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def reflect_x(point):
#         return Point(point.x, -point.y)


# 3. Add a method slope_from_origin which returns the slope of the line joining the origin to the
# point. For
# example:
# 1 >>> Point(4, 10).slope_from_origin()
# 2 2.5
# What cases will cause this method to fail? 
# answer: when x value equal to 0

# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def slope_from_origin(self):
#         return (self.y - 0)/(self.x - 0)

# print(Point(4, 10).slope_from_origin())


# 4. The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients a and b
# completely describe the line. Write a method in the Point class so that if a point instance is
# given another point, it will compute the equation of the straight ine joining the two points. It must
# return the two coefficients as a tuple of two values. For example, :
# 1 >>> print(Point(4, 11).get_line_to(Point(6, 15)))
# 2 >>> (2, 3)
# This tells us that the equation of the line joining the two points is “y = 2x + 3”. When will this method
# fail? answer: this method will fail if (x1 - x2) == 0

# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def get_line_to(self, point):
#         # formula (y - y1)/(y2 - y1) = (x - x1)/(x2 - x1)
#         # x2 = point y2 = point
#         # x1 = self  y1 = self
#         cone = (point.y - self.y) / (point.x - self.x)
#         box = (-(point.y - self.y) * self.x) + ((point.x - self.x) * self.y)
#         box = box / (point.x - self.x)
#         return (int(cone), int(box))

# print(Point(4, 11).get_line_to(Point(6, 15)))


# 5. Given four points that fall on the circumference of a circle, find the midpoint of the circle. When
# will this function fail? unfinished
# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

# def midpoint(p1, p2):
#     """Return the midpoint of p1 and p2"""
#     mx = (p1.x + p2.x)/2
#     my = (p1.y + p2.y)/2
#     return Point(mx, my)

# def midpoint_circle(a, b, c, d):
#     # find ab gradient
#     ab_m = (b.y -a.y) / (b.x - a.x)
#     mid_ab = midpoint(a, b)
#     normal_ab_m = -(1/(ab_m))
    
#     cd_m = (d.y -c.y) / (d.x - c.x)
#     mid_cd = midpoint(c, d)
#     normal_cd_m = -(1/(cd_m))




midpoint_circle(Point(-7, 7), Point(1, 9), Point(3, 1), Point(-7, 1))



# 6. Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox
# or outbox on a cellphone:
# 1 my_inbox = SMS_store()

# This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages). Each
# message will be represented as a tuple:
# 1 (has_been_viewed, from_number, time_arrived, text_of_SMS)

class SMS_store:
    message = []

    def __str__(self):
        return str(self.message)
    
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its
        # has_been_viewed status is set False.
        has_been_viewed = False
        self.message.append([has_been_viewed, from_number, time_arrived, text_of_SMS])
    
    def message_count(self):
        # Returns the number of sms messages in my_inbox
        return len(self.message)

    def get_unread_indexes(self):
        # Returns list of indexes of all not-yet-viewed SMS messages
        unread = []
        for i, message in enumerate(self.message):
            if message[0] == False:
                unread.append(i)
        return unread

    def get_message(self, i):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
        if i in range(len(self.message)):
            self.message[i][0] = True
            return self.message[i][1:]
        else:
            return None
    
    def delete(self, i):
        # Delete the message at index i
        del self.message[i]

    def clear(self):
        # Delete all messages from inbox
        self.message.clear()

myinbox = SMS_store()
myinbox.add_new_arrival(12345, '9am', 'helloworld!')
myinbox.add_new_arrival(12, '10am', 'cat')
myinbox.add_new_arrival(213120, '12pm', 'dog')
print(myinbox)
print('message exist:', myinbox.message_count())
print('unread messages:', myinbox.get_unread_indexes())
print(myinbox.get_message(0))
print(myinbox.get_message(4))
print('unread messages:', myinbox.get_unread_indexes())
myinbox.delete(0)
print(myinbox)
myinbox.clear()
print(myinbox)
