import sys


# 1. Write a function to count how many odd numbers are in a list.
def count_odd_nums(num_list):
    counter = 0
    for num in num_list:
        if num % 2 == 1:
            counter += 1
    return counter


# 2. Sum up all the even numbers in a list
def sum_even_nums(num_list):
    total = 0
    for num in num_list:
        if num % 2 == 0:
            total += num
    return total


# 3. Sum up all the negative numbers in a list.
def sum_negative_nums(num_list):
    total = 0
    for num in num_list:
        if num < 0:
            total += num
    return total


# 4. Count how many words in a list have length 5.
def count_word(word_list):
    counter = 0
    for word in word_list:
        if len(word) == 5:
            counter += 1
    return counter


# 5. Sum all the elements in a list up to but not including the first even number. (Write your unit
# tests. What if there is no even number?)
def sum_without_firste(num_list):
    total = 0
    first = True
    for num in num_list:
        if first == True and num % 2 == 0:
            first = False
            continue
        else:
            total += num
    return total

# 6. Count how many words occur in a list up to and including the first occurrence of the word
# “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
def count_till_sam(word_list):
    counter = 0
    for word in word_list:
        if word == 'sam':
            break
        else:
            counter += 1
    return counter


# 7. Add a print function to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.
def sqrt(n):
    counter = 0
    approx = n/2.0 # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better, counter
        approx = better
        counter += 1
# 8. Trace the execution of the last version of print_mult_table and figure out how it works.
def print_multiples(n):
    res = ''
    for i in range(1,7):
        res += str(n * i) + '\t'
    res += '\t\n'
    return res


def print_mult_table():
    text = ''
    for i in range(1, 7):
        print('Iterasi',i)
        text += print_multiples(i)
        print(text)


# 9. Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A
# call to print_triangular_numbers(5) would produce the following output:
# 1 1 1
# 2 2 3
# 3 3 6
# 4 4 10
# 5 5 15
# (hint: use a web search to find out what a triangular number is.)
def print_triangular_numbers(n):
    counter = 0
    result = 0
    for i in range(n):
        counter += 1
        result += counter
        print(counter, '\t',result)


# 10. Write a function, is_prime, which takes a single integer argument and returns True when the
# argument is a prime number and False otherwise. Add tests for cases like this:
def is_prime(n):
    factor = 0
    for i in range(1,n+1):
        if n % i == 0 and n % 1 == 0:
            factor += 1
    if factor == 2:
        return True
    return False


# 14. What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_-
# digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that
# it works correctly with any integer value. Add these tests:
def num_digits(n):
    count = 0 
    num = abs(n)
    if num == 0:
        return 1
    else:
        while num != 0:
            count += 1
            num //= 10
    return count


def num_even_digits(n):
    count = 0 
    even = 0
    num = abs(n)
    if num == 0:
        return 1
    else:
        while num != 0:
            count += 1
            if num % 2 == 0:
                even += 1
            num //= 10
    return even


# 16. Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in
# the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
def sum_of_squares(xs):
    result = 0
    for i in xs:
        result += i ** 2
    return result


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
    # # 1.
    # test(count_odd_nums([1,2,3,4,5]) == 3)
    # test(count_odd_nums([22,44,66]) == 0)
    # test(count_odd_nums([-1]) == 1)
    
    # # 2.
    # test(sum_even_nums([1,2,3,4,5]) == 6)
    # test(sum_even_nums([22,44,66]) == 132)
    # test(sum_even_nums([-1]) == 0)

    # # 3.
    # test(sum_negative_nums([1,2,3,4,5]) == 0)
    # test(sum_negative_nums([22,44,66]) == 0)
    # test(sum_negative_nums([-1]) == -1)
    # test(sum_negative_nums([-1,-22,-333]) == -356)

    # # 4. 
    # test(count_word(['hello','hey','yes','world']) == 2)
    # test(count_word(['hello','hey','yes','world!']) == 1)
    
    # # 5. 
    # # if there is no even number in list, summification still works
    # test(sum_without_firste([1,2,3,4,5]) == 13)
    # test(sum_without_firste([22,44,66]) == 110)
    # test(sum_without_firste([-1]) == -1)

    # # 6. if 'sam' doesn't occur, the program will count all elements in the list
    # test(count_till_sam(['eddie', 'steve', 'bob', 'sam']) == 3)
    # test(count_till_sam(['sam', 'eddie', 'steve', 'bob']) == 0)
    # test(count_till_sam(['eddie', 'steve', 'bob']) == 3)

    # # 7. 
    # sqrt(25)

    # result
    # 7.25
    # 5.349137931034482
    # 5.011394106532552
    # 5.000012953048684
    # 5.000000000016778

    # # 10.
    # test(is_prime(11))
    # test(not is_prime(35))
    # test(is_prime(19911121))
    
    # 14.
    # test(num_digits(0) == 1)
    # test(num_digits(-12345) == 5)

    # 15.
    # test(num_even_digits(123456) == 3)
    # test(num_even_digits(2468) == 4)
    # test(num_even_digits(1357) == 0)
    # test(num_even_digits(0) == 1)

    # 16.
    # test(sum_of_squares([2, 3, 4]) == 29)
    # test(sum_of_squares([ ]) == 0)
    # test(sum_of_squares([2, -3, 4]) == 29)

test_suite()

# print_mult_table()

# print_triangular_numbers(5)


# # 11. Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk pirate
# # makes a turn, and then takes some steps forward, and repeats this. Our social science student
# # now records pairs of data: the angle of each turn, and the number of steps taken after the turn.
# # Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Use a turtle to draw the path
# # taken by our drunk friend.

# import turtle
# import random

# screen = turtle.Screen()
# tess = turtle.Turtle()

# rand_angle =  [(160, 20), (-43, 10), (270, 8), (-43, 12)]
# for i in range(100):
#     direction = rand_angle[random.randint(0, 3)]
#     if direction[0] > 0:
#         tess.left(direction[0])
#     else:
#         tess.right(direction[0])
#     tess.forward(direction[1])

#     if i == 99:
#         print(direction)

# screen.mainloop()


# 12. Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn, and the second item is the distance to move
# forward. Set up a list of pairs so that the turtle draws a house with a cross through the centre,
# as show here. This should be done without going over any of the lines / edges more than once,
# and without lifting your pen.
# import turtle

# tess = turtle.Turtle()
# wn = turtle.Screen()

# tess.left(90)
# tess.forward(50)
# tess.left(45)
# tess.forward(50)
# tess.left(90)
# tess.forward(50)
# tess.left(45)
# tess.forward(50)
# tess.left(90)
# tess.forward(70)
# tess.left(145)
# tess.forward(86)
# tess.right(145)
# tess.forward(70)
# tess.right(145)
# tess.forward(86)

# wn.mainloop()


# 13. Not all shapes like the one above can be drawn without lifting your pen, or going over an edge
# more than once. Which of these can be drawn? 1, 2, 5, 6 

# 17. You and your friend are in a team to write a two-player game, human against computer, such
# as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one round of
# the game, while you will write the logic to allow many rounds of play, keep score, decide who
# plays, first, etc. The two of you negotiate on how the two parts of the program will fit together,
# and you come up with this simple scaffolding (which your friend will improve later):

# Your friend will complete this function
def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """

    # This is all dummy scaffolding code right at the moment...
    import random # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} "
        .format(human_plays_first, result))

    return result

# a. Write the main program which repeatedly calls this function to play the game, and after
# each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”. It then
# asks the player “Do you want to play again?” and either plays again, or says “Goodbye”,
# and terminates.

# b. Keep score of how many wins each player has had, and how many draws there have been.
# After each round of play, also announce the scores.

# c. Add logic so that the players take turns to play first

# d. Compute the percentage of wins for the human, out of all games played. Also announce
# this at the end of each round.

# e. Draw a flowchart of your logic.

def percentage(human, draw, comp):
    """Function to calculate the percentage of human winning rate."""
    total = human + draw + comp
    if human != 0:
        return (human / total ) * 100
    else:
        return 0.0

def main():
    """Main program of the case(game)."""
    human_score = 0
    comp_score = 0
    draws = 0
    human_first = bool(input('human want to play first?(True/False) '))

    while True:
        res = play_once(human_first)
        if res == -1:
            human_score += 1
            print('Human win!')
        elif res == 0:
            draws += 1
            print('Game Drawn!')
        elif res == 1:
            comp_score += 1
            print('Comp win!')

        print("-----\nScore => Human:{0}, Draws:{1}, Comp:{2}\nPercentage or human wins game: {3:.2f}\n-----\n"
            .format(human_score, draws, comp_score,percentage(human_score, draws, comp_score) ),end='')
        again = input('Do you want to play again?(y/n): ')
        print('')

        if again == 'n':
            print('\n Goodbye \n')
            break


main()