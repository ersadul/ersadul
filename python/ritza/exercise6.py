import sys


def turn_clockwise(direct):
    if direct == 'W':
        return 'N'
    elif direct == 'N':
        return 'E'
    elif direct == 'E':
        return 'S'
    elif direct == 'E':
        return 'W'
    else:
        return 


def day_name(n):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if n <= 6:
        return days[n]
    else:
        return


def day_num(day):
    days = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
    if day in days:
        return days[day]
    else:
        return 


def day_add(day, delta):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if delta > 7 or delta < 7:
        return days[(day_num(day) + delta % 7) % 7]


def days_in_month(month):
    months = {'January': 31, 'February':28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    if month in months:
        return months[month]
    else: 
        return


def to_secs(hour, minute, second):
    return int((hour * 3600) + (minute * 60) + second)


def hours_in(secs):
    return secs // 3600


def minutes_in(secs):
    return (secs // 60) % 60


def seconds_in(secs):
    return secs - (to_secs(hours_in(secs), 0, 0) + to_secs(0, minutes_in(secs), 0))


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def hypotenuse(leg1, leg2):
    return ((leg1**2) + (leg2**2)) ** 0.5


def slope(x1, y1, x2, y2):
    return (y2 - y1 )/ (x2 - x1)


def intercept(x1, x2, y1, y2):  #FAILED
    return y1 (slope(x1, y1, x2, y2) * x1)  #FAILED


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return is_even(n) # modified


def is_factor(f, n):
    if n % f == 0:
        return True
    else:
        return False


def is_multiple(a, b):
    return is_factor(b, a)


def f2c(t):
    return round((t - 32) * 5/9)


def c2f(t):
    return round((t * 9/5) + 32)


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} failed.'.format(linenum)
    print(msg)


def test_suite():
    """ Run the suite of test for code in this module. """
    # test(turn_clockwise("N") == "E")
    # test(turn_clockwise("W") == "N")
    # test(turn_clockwise(42) == None)
    # test(turn_clockwise("rubbish") == None)

    # test(day_name(3) == "Wednesday")
    # test(day_name(6) == "Saturday")
    # test(day_name(42) == None)

    # test(day_num("Friday") == 5)
    # test(day_num("Sunday") == 0)
    # test(day_num(day_name(3)) == 3)
    # test(day_name(day_num("Thursday")) == "Thursday")
    # test(day_num("Halloween") == None)
    
    # test(day_add("Monday", 4) == "Friday")
    # test(day_add("Tuesday", 0) == "Tuesday")
    # test(day_add("Tuesday", 14) == "Tuesday")
    # test(day_add("Sunday", 100) == "Tuesday")

    # test(day_add("Sunday", -1) == "Saturday")
    # test(day_add("Sunday", -7) == "Sunday")
    # test(day_add("Tuesday", -100) == "Sunday")

    # test(days_in_month("February") == 28)
    # test(days_in_month("December") == 31)

    # test(to_secs(2, 30, 10) == 9010)
    # test(to_secs(2, 0, 0) == 7200)
    # test(to_secs(0, 2, 0) == 120)
    # test(to_secs(0, 0, 42) == 42)
    # test(to_secs(0, -10, 10) == -590)

    # test(to_secs(2.5, 0, 10.71) == 9010)
    # test(to_secs(2.433,0,0) == 8758)

    # test(hours_in(9010) == 2)
    # test(minutes_in(9010) == 30)
    # test(seconds_in(9010) == 10)

    # test(3 % 4 == 0)    # cos 3 modulo 4 is 3
    # test(3 % 4 == 3)
    # test(3 / 4 == 0)    # cos 3 divided by 4 is 0.75
    # test(3 // 4 == 0)
    # test(3+4 * 2 == 14) # cos 12 != 14
    # test(4-2+2 == 0)    # cos 4 != 0
    # test(len("hello, world!") == 13)

    # test(compare(5, 4) == 1)
    # test(compare(7, 7) == 0)
    # test(compare(2, 3) == -1)
    # test(compare(42, 1) == 1)

    # test(hypotenuse(3, 4) == 5.0)
    # test(hypotenuse(12, 5) == 13.0)
    # test(hypotenuse(24, 7) == 25.0)
    # test(hypotenuse(9, 12) == 15.0)

    # test(slope(5, 3, 4, 2) == 1.0)
    # test(slope(1, 2, 3, 2) == 0.0)
    # test(slope(1, 2, 3, 3) == 0.5)
    # test(slope(2, 4, 1, 2) == 2.0)

    # test(intercept(1, 6, 3, 12) == 3.0)   #FAILED
    # test(intercept(6, 1, 1, 6) == 7.0)    #FAILED
    # test(intercept(4, 6, 12, 8) == 5.0)   #FAILED

    # test(is_even(4))
    # test(is_even(2))
    # test(is_even(21))

    # test(is_odd(1))
    # test(is_odd(2))
    # test(is_odd(55))

    # test(is_factor(3, 12))
    # test(not is_factor(5, 12))
    # test(is_factor(7, 14))
    # test(not is_factor(7, 15))
    # test(is_factor(1, 15))
    # test(is_factor(15, 15))
    # test(not is_factor(25, 15))

    # test(is_multiple(12, 3))
    # test(is_multiple(12, 4))
    # test(not is_multiple(12, 5))
    # test(is_multiple(12, 6))
    # test(not is_multiple(12, 7))

    # test(f2c(212) == 100) # Boiling point of water
    # test(f2c(32) == 0) # Freezing point of water
    # test(f2c(-40) == -40) # Wow, what an interesting case!
    # test(f2c(36) == 2)
    # test(f2c(37) == 3)
    # test(f2c(38) == 3)
    # test(f2c(39) == 4)

    # test(c2f(0) == 32)
    # test(c2f(100) == 212)
    # test(c2f(-40) == -40)
    # test(c2f(12) == 54)
    # test(c2f(18) == 64)
    # test(c2f(-48) == -54)


test_suite()

