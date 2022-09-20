# 1. We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
# Construct a small Python example to test whether this is possible, and write up your findings
def print_function(n):
    print('result', n)

print_function((2,3))

# 2. Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?
# tuple is a generalization of a pair, because we can say that pair can be tuple, but tuple not only pair, in other way there is triplet, quantuplet, ext.

# 3. Is a pair a kind of tuple, or is a tuple a kind of pair?
# pair kind of tuple