import sys
import string


def remove_vowels(text):
    vowels = 'aiueoAIUEO'
    text_sans_vowels = ''
    for char in text:
        if char not in vowels:
            text_sans_vowels += char
    return text_sans_vowels
    

def find(text, char, start = 0, end = None):
    """
    Find and return the index of char in text.
    Return -1 if char doesn't occur in text.
    """
    iChar = start
    if end is None:
        end = len(text)
    while iChar < end:
        if text[iChar] == char:
            return iChar
        iChar += 1
    return -1


def count_a(text):
    counter = 0
    for char in text:
        if char == 'a':
            counter += 1
    return counter


def find2(text, char, start):
    iChar = start
    while iChar < len(text):
        if text[iChar] == char:
            return iChar
        iChar += 1
    return -1
    

def remove_punctuation(text):
    text_sans_punct = ''
    for letter in text:
        if letter not in string.punctuation:
            text_sans_punct += letter
    return text_sans_punct

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
    # test(remove_vowels("compsci") == "cmpsc")
    # test(remove_vowels("aAbEefIijOopUus") == "bfjps")   

    # test(find("Compsci", "p") == 3)
    # test(find("Compsci", "C") == 0)
    # test(find("Compsci", "i") == 6)
    # test(find("Compsci", "x") == -1)

    # test(count_a("banana") == 3)

    # test(find2("banana", "a", 2) == 3)

    # ss = "Python strings have some interesting methods."
    # test(find(ss, "s") == 7)
    # test(find(ss, "s", 7) == 7)
    # test(find(ss, "s", 8) == 13)
    # test(find(ss, "s", 8, 13) == -1)
    # test(find(ss, ".") == len(ss)-1)

    # test(remove_punctuation('"Well, I never did!", said Alice.') == "Well I never did said Alice")
    # test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")




test_suite()

# my_story = """
# Pythons are constrictors, which means that they will 'squeeze' the life
# out of their prey. They coil themselves around their prey and with
# each breath the creature takes the snake will squeeze a little tighter
# until they stop breathing completely. Once the heart stops the prey
# is swallowed whole. The entire animal is digested in the snake's
# stomach except for fur or feathers. What do you think happens to the fur,
# feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
# you guessed it --- snake POOP! """

# wds = remove_punctuation(my_story).split()
# print(wds)

# s1 = "His name is {0}!".format("Arthur")
# print(s1)

# name = "Alice"
# age = 10
# s2 = "I am {1} and I am {0} years old.".format(age, name)
# print(s2)

# n1 = 4
# n2 = 5
# s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
# print(s3)

# print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
# for i in range(1, 11):
#     print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t", i**10, "\t", i**20)

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
