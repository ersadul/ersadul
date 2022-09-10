import sys


def mysum(xs):
    """Sum all the number in the list xs, and return the total."""
    running_total = 0
    for x in xs:
        running_total += x
    return running_total


def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    total = 0
    counter = 1
    while counter <= n:
        total += counter
        counter += 1
    return total


def seq3np1(n):
    """ Print the 3n+1 sequence from n, 
        terminating when it reaches 1. """
    while n!= 1:
        print(n, end=', ')
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 +1
    print(n, end='.\n')


def num_digits(n):
    count = 0 
    while n != 0:
        count += 1
        n //= 10
    return count


# Notice, however, that test(num_digits(0) == 1) fails. Explain why. Do you think this is a bug in
# the code, or a bug in the specifications, or our expectations, or the tests? 
# it's a bug in code, because the purpose in this function to count either zero or five. so if we insert number zero into the function 
# it must count as 1
def num_zero_and_five_digits(n):
    count = 0
    if n ==  0:
        return 1

    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count


def print_multiples(n):
    for i in range(1,7):
        print(n *i, end='\t')
    print()


def print_mult_table():
    for i in range(1, 7):
        print_multiples(i)

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
    # test(mysum([1, 2, 3, 4]) == 10)
    # test(mysum([1.25, 2.5, 1.75]) == 5.5)
    # test(mysum([1, -2, 3]) == 2)
    # test(mysum([ ]) == 0)
    # test(mysum(range(11)) == 55) # 11 is not included in the list.

    # test(sum_to(4) == 10)
    # test(sum_to(1000) == 500500)


# test_suite()


# print(num_zero_and_five_digits(150))

# for x in range(13):
#     print(x, '\t', 2**x)

# for i in range(1,7):
#     print(2 * i, end='   ')
# print()

# print_multiples(3)
# print_multiples(4)
# for i in range(1,7):
#     print_multiples(i)
# print_mult_table()

# for i in [12, 16, 17, 24, 29]:
#     if i % 2 == 1:  # if the number i is odd
#         break       # then break the loop / immidiatly exit the loop
#     print(i)
# print('done')


# total = 0
# while True:
#     response = input('Enter the next number. (leave black to end)')
#     if response == '':
#         break
#     total += int(response)

# print('The total of the numbers you entered is ', total)


# import random
# rng = random.Random()
# number = rng.randrange(1, 1000)

# guesses = 0
# msg = ''

# while True:
#     guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
#     guesses += 1

#     if guess > number:
#         msg += str(guess) + ' is too high.\n'
#     elif guess < number:
#         msg += str(guess) + ' is too low.\n'
#     else:
#         break
# input('\n\nGreat, you got it in {0} guesses!\n\n'.format(guesses))


# for i in [12, 16, 17, 24, 29, 30]:
#     if i % 2 == 1:
#         continue
#     print(i)
# print('done')


# celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937),("Justin Bieber", 1994)]
# # print(len(celebs))

# for (nm, yr) in celebs:
#     if yr < 1980:
#         print(nm)


# students = [
#     ("John", ["CompSci", "Physics"]),
#     ("Vusi", ["Maths", "CompSci", "Stats"]),
#     ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
#     ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
#     ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# # Print all students with a count of their courses.
# for (name, subjects) in students:
#     print(name, 'takes', len(subjects), 'courses: ', end='')
#     for subject in subjects:
#         print(subject+ ", ", end='')
#     print(end='\n')

# # Count how many students are taking CompSci
# counter = 0
# for (name, subjects) in students:
#     for subject in subjects:
#         if subject == 'CompSci':
#             counter += 1
# print('The number of students taking CompSci is', counter)

# def sqrt(n):
#     counter = 0
#     approx = n/2.0 # Start with some or other guess at the answer
#     while True:
#         better = (approx + n/approx)/2.0
#         if abs(approx - better) < 0.001:
#             return better, counter
#         approx = better
#         counter += 1
# # Test cases
# print(sqrt(25.0))
# print(sqrt(49.0))
# print(sqrt(81.0))
