import sys


# 7. Write a function that reverses its string argument, and satisfies these tests:
def reverse(text):
    return text[::-1]


# 8. Write a function that mirrors its argument:
def mirror(text):
    return text + reverse(text)

# 9. Write a function that removes all occurrences of a given letter from a string:
def remove_letter(letter, text):
    result = ''
    for char in text:
        if char == letter:
            continue
        result += char
    return result


# 10. Write a function that recognizes palindromes. (Hint: use your reverse function to make this
# easy!):
def is_palindrome(text):
    if text == reverse(text):
        return True
    return False


# 11. Write a function that counts how many times a substring occurs in a string:
def count(sub, text):
    temp = ''
    counter = 0
    for i in range(len(text)):
        temp = text[i:len(text)]
        if temp[0:len(sub)] == sub:
            counter += 1
    return counter


# 12. Write a function that removes the first occurrence of a string from another string:
def remove(sub, text):
    result = ''
    temp = ''
    iSub = 0
    first_occurence = False
    for i in range(len(text)):
        if first_occurence == True:
            result = result[0:len(result)-1]
            break
        iSub +=1
        temp = text[i:len(text)]
        result += temp[0]
        if temp[0:len(sub)] == sub:
            first_occurence = True
    result += text[len(result)+len(sub):]
    return result


# 13. Write a function that removes all occurrences of a string from another string:
def remove_all(sub, text):
    temp = ''
    temp = remove(sub, text)
    while True:
        if sub in temp:
            temp = remove(sub, temp)
        else:
            break
    return temp



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
    # test(reverse("happy") == "yppah")
    # test(reverse("Python") == "nohtyP")
    # test(reverse("") == "")
    # test(reverse("a") == "a")

    # test(mirror("good") == "gooddoog")
    # test(mirror("Python") == "PythonnohtyP")
    # test(mirror("") == "")
    # test(mirror("a") == "aa")

    # test(remove_letter("a", "apple") == "pple")
    # test(remove_letter("a", "banana") == "bnn")
    # test(remove_letter("z", "banana") == "banana")
    # test(remove_letter("i", "Mississippi") == "Msssspp")
    # test(remove_letter("b", "") == "")
    # test(remove_letter("b", "c") == "c")

    # test(is_palindrome("abba"))
    # test(not is_palindrome("abab"))
    # test(is_palindrome("tenet"))
    # test(not is_palindrome("banana"))
    # test(is_palindrome("straw warts"))
    # test(is_palindrome("a"))
    # test(is_palindrome("")) # Is an empty string a palindrome?

    # test(count("is", "Mississippi") == 2)
    # test(count("an", "banana") == 2)
    # test(count("ana", "banana") == 2)
    # test(count("nana", "banana") == 1)
    # test(count("nanan", "banana") == 0)
    # test(count("aaa", "aaaaaa") == 4)

    # test(remove("an", "banana") == "bana")
    # test(remove("cyc", "bicycle") == "bile")
    # test(remove("iss", "Mississippi") == "Missippi")
    # test(remove("eggs", "bicycle") == "bicycle")

    # test(remove_all("an", "banana") == 'ba')
    # test(remove_all("cyc", "bicycle") == 'bile')
    # test(remove_all("iss", "Mississippi") == 'Mippi')
    # test(remove_all("eggs", "bicycle") == 'bicycle')


test_suite()

# 1. What is the result of each of the following:
    # >>> "Python"[1]                   >> 'y'
    # >>> "Strings are sequences of characters."[5] >> 'g'
    # >>> len("wonderful")              >> 9
    # >>> "Mystery"[:4]                 >> 'Myst'
    # >>> "p" in "Pineapple"            >> True
    # >>> "apple" in "Pineapple"        >> True
    # >>> "pear" not in "Pineapple"     >> True
    # >>> "apple" > "pineapple"         >> False
    # >>> "pineapple" < "Peach"         >> False


# 2. Modify:
# so that Ouack and Quack are spelled correctly.
# prefixes = "JKLMNOPQ"
# suffix = "uack"

# for letter in prefixes:
#     print(letter + suffix)

# 3. Encapsulate
# fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

# 3. Encapsulate
# in a function named count_letters, and generalize it so that it accepts  the string and the letter as
# arguments. Make the function return the number of characters, rather than print the answer. The
# caller should do the printing.

def find(text, letter, start = 0, end = None):
    """
    Find and return the index of char in text.
    Return -1 if char doesn't occur in text.
    """
    iLetter = start
    if end is None:
        end = len(text)
    while iChar < end:
        if text[iLetter] == letter:
            return iChar
        iLetter += 1
    return -1

def count_letters(text, letter):
    counter = 0
    for char in text:
        if char == 'a':
            counter += 1
    return counter

# 4. Now rewrite the count_letters function so that instead of traversing the string, it repeatedly
# calls the find method, with the optional third parameter to locate new occurrences of the letter
# being counted.

# 5. Assign to a variable in your program a triple-quoted string that contains your favourite
# paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational
# verses, etc.
# Write a function which removes all punctuation from the string, breaks the string into a list of
# words, and counts the number of words in your text that contain the letter “e”. Your program
# should print an analysis of the text like this:

# I DONT EVEN UNDERSTAND THE 2 QUESTIONS ABOVE :O
# so, i skipped these questions

# 6. Print a neat looking multiplication table like this:

# layout = "{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}"
# print(layout.format('  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
# print(' :--------------------------------------------------')
# for i in range(1,13):
#     print(layout.format(str(i)+':', i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))
