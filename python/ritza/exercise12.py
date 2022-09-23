from unit_tester import test

# 7.
def replace(s, old, new):
    if len(old) == 1:
        words = [ch for ch in s]
        for i, word in enumerate(words):
            if word == old:
                words[i] = new

        return ''.join(words)

    else:
        words = s.split()
        for i, word in enumerate(words):
            if old in word:
                words[i] = word[:word.index(old)] + new + word[word.index(old)+len(old):]
                
        return ' '.join(words)

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    return new.join(s.split(old))

# test(myreplace(",", ";", "this, that, and some other thing") ==
# "this; that; and some other thing")
# test(myreplace(" ", "**",
# "Words will now be separated by stars.") ==
#  "Words**will**now**be**separated**by**stars.")

# 8.
def cleanword(word):
    symbol = "`~!@#$%^&*()_+-=[];':\|,./<>?\{\}"
    result = ''
    for char in word:
        if char in symbol:
            continue
        result += char
    
    return result


def has_dashdash(word):
    if '--' in word:
        return True
    return False


def extract_words(word):
    if '--' in word:
        words = word.split('--')
        word = ' '.join(words)
    words = word.split()
    result = []
    for word in words:
        result.append(str.lower(cleanword(word)))

    return result

def wordcount(target, words):
    counter = 0
    for word in words:
        if word == target:
            counter += 1
    return counter


def wordset(words):
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    result.sort()
    return result


def longestword(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

# test(cleanword("what?") == "what")
# test(cleanword("'now!'") == "now")
# test(cleanword("?+='w-o-r-d!,@$()'") == "word")

# test(has_dashdash("distance--but"))
# test(not has_dashdash("several"))
# test(has_dashdash("spoke--"))
# test(has_dashdash("distance--but"))
# test(not has_dashdash("-yo-yo-"))

# test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is'\
# ,'the','time','now','is','the','time','yes','now'])
# test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to'\
# ,'curtsey','as','she','spoke','fancy'])

# test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
# test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
# test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
# test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

# test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
# test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
# test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are"\
# , "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)