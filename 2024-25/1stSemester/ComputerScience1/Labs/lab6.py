# CS1210: Lab6 [4 functions to complete]
######################################################################
# READ ALL INSTRUCTIONS CAREFULLY.
#
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partner(s), and
#  2) you have not shared it nor will share it with anyone else.
#
# ToDo: Change the two "hawkid" strings to match the hawkids of you
# and your partner(s). Your hawkid is the "login identifier" that you
# use to login to all University services: it is not your email
# address or your student id number.
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "segre". 
#
# Note: if there are 3 of you, add a third string to the list returned
# by signed() below (e.g., change ["hawkid1","hawkid2"] to
# ["hawkid1","hawkid2","hawkid3"], using your own three UI login
# identifiers as the hawkid values).
#
def signed():
    return(["mgarcia42","cmcano"])

######################################################################
# Specification: biggestI(S, result) returns the maximum value int or
# float found within the sequence S, which contains only ints or
# floats. Your function should use the appropriate iterative form, and
# it should work for both lists and tuples.
#
# Example:
#   >>> biggestI((1, 2.8, 3, 3.0))
#   3.0
#   >>> biggestI([5, 3, 1, -1, -3, -5, -7])
#   5
#
# Essentially, biggestI(S) is a home-built version of max(S), but with
# one critical difference illustrated here:
#
#   >>> biggestI([])          # No max in empty S!
#   >>> max([])
#   Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#   ValueError: max() arg is an empty sequence
#
# Note that the signature to biggestI contains an optional value,
# result, which you should feel free to use in your solution. The fact
# that it's initially set to None, the value returned for an empty S,
# is not coincidental.
#
def biggestI(S, result=None):
    for x in S:
        if S == []:
            return None
        elif x > S[0]:
            result = x
        elif x < S[0]:
            result = S[0]
    return result
print(biggestI((1, 2.8, 3, 3.0)))
print(biggestI([2, 3, 1, -1, 5, -5, -7]))

######################################################################
# Specification: biggestR(S, result) is the recursive form of
# biggestI() above.
#
# Your solution should be purely recursive: it should not make use of
# any form of iteration (for, while or comprehension): feel free to
# review the solution to QotD14 for inspiration.
#
# Again, the optional argument result (initially None) is used to
# "carry in" a default value: your recursive solution can rely on
# explicitly passing a different value of result in each recursive
# call.
#
def biggestR(S, result=None):
    if len(S)==0:
        return result
    if result is None or result < S[0]:
        result = S[0]
    return biggestR(S[1:],result)

        

######################################################################
# Specification: biggestD(S, result=None) is an extension of
# biggestR(S, result=None) that also operates correctly on nested
# structures, S. A nested structure is composed of ints, floats, lists
# or tuples which can also be nested, that is, each list or tuple
# might contain other lists or tuples.
#
# As before, your solution should be purely recursive, and should not
# make use of any form of iteration.
#
# Example:
#   >>> biggestD([1.0, [[2]], (3, 4.8), (6, -2, -3)])
#   6
#   >>> biggestD(([], (), [([])]))        # Again, no max for empty S!
#   >>> biggestD((1.0, [[7.0], -3.0], -17.2, [(3, 2), [], 6.5]))
#   7.0
#
# This is actually somewhat tricky. 
#
# Also, if it helps, recall that, e.g.,
#   >>> type(3.0) in (int, float)
#   True
#   >>> type([1, 2]) is list
#   True
#   >>> type((1,)) is tuple
#   True
#
def biggestD(S, result=None):
    if len(S) == 0:
        return result
    elif type(S[0]) in (int,float):
        if result is None or result < S[0]:
            result = S[0]
        return biggestD(S[1:],result)
    else:
        return biggestD(S[1:],(biggestD(S[0],result)))

