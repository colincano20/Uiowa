# CS1210: Lab8 [4 functions to complete]
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
    return(["cmcano","bedouglas"])

######################################################################
# You will recognize these Midterm2 problems. Because Midterm2
# problems are problems that you should be able to solve at this point
# in the class, I thought I'd give everyone a second chance to really
# work through these, discuss them with a partner, and implement/test
# them in Python to cement your understanding of these concepts.
######################################################################
# Specification: countExtras(S) takes a sequence, S, and returns an
# integer indicating how many elements of S are duplicates.
#
# Examples:
#   >>> countExtras((1, 2, 3, 1, 1, 4, 5))
#   2        # two extra 1's
#   >>> countExtras(range(100))
#   0        # not hard to understand why
#   >>> countExtras("the rain in spain falls mainly in the plains")
#   30       # +4a, +5n, +5i, +1e, +1p, +3l, +2s, +1t, +1h, and +7 spaces
#
# Using sets
def countExtras(S):
    count = set()
    result = 0
    for i in S:
        if i in count:
            result += 1
        else:
            count.add(i)
    return result

        

######################################################################
# Specification: Specification: countPeaks(S) takes a sequence, S, and
# returns an integer representing the number of ``peaks'' in S.
#
# A peak is an index, 0 <= i < len(S) where S[i] is greater than or
# equal to S[i-1] and S[i] is greater than S[i+1] (\fIi.e.\fP, S[i] is
# followed directly by a drop in value, where S[0] follows S[-1]).
#
# Your solution should use an appropriate form of iteration, and
# should work for lists, tuples, strings, and ranges:
#
# Example:
#   >>> countPeaks(range(10))
#   1
#   >>> countPeaks((1, 3, 2, 4, 6, 10, 9, 7, 7))
#   3
#   >>> countPeaks('AaBbCcDd')
#   4
#
def countPeaks(S):
    count = 0
    for i in range(len(S)-1):
        if S[i] >= S[i-1] and S[i] > S[i+1]:
            count += 1
    if S[-1] >= S[-2] and S[-1] > S[0]:
            count +=1
    return count


######################################################################
# Specification: stringify(S, c) takes a structure, S, consisting
# of (possibly nested) lists, tuples, sets, and other printable elements
# (ints, floats, or strings, but not dictionaries) and returns a string
# that contains all of these printable elements, in order, separated by
# character c.
#
# Examples:
#   >>> stringify((0, ["paper", 3, 1], [[(range(4, 16, 3))]]))
#   '0.paper.3.1.4.7.10.13'
#   >>> stringify([[1, 2, 'abc', (3, 4.0, 'xyq'), 'uf'], 3], '|')
#   '1|2|abc|3|4.0|xyq|uf|3'
#   >>> stringify(({'alpha'}, (), [[['omega']]], []), ':')
#   'alpha:omega'  # and not 'alpha::omega'
#
# For full credit, make sure there are no extra spurious separating
# characters in the result, but without also dropping the 0 in the
# first example.
#
def stringify(S, c='.'):
    if isinstance(S,(list,tuple,set,range)):
        return c.join([stringify(x,c) for x in S if x or x == 0])
    return(str(S))




######################################################################
# Specification: findExtras(S, skip=()) takes a sequence, S, and a
# tuple, skip, and returns the set of replicated elements in S,
# excluding any elements of skip.
#
# Examples:
#   >>> findExtras((1, 2, 3, 1, 1, 4, 5))
#   {1}
#   >>> findExtras("the rain in spain falls mainly in the plains", ('the ',))
#   {'n', 'a', 'i', 'p', 'l', 's'}
#
# You will note this problem closely resembles Problem 1, except for
# the extra skip parameter and the fact that we collect and return the
# set of duplicated elements rather than just counting them.
#
# Your solution should be strictly recursive, and should work for
# lists, tuples, strings and ranges.
#
def findExtras(S, skip=()):
    if len(S) == 0:
        return set()
    result = findExtras(S[1:], skip)
    if S[0] not in skip and S[0] in S[1:]:
        result.add(S[0])
    return result

print(findExtras((1, 2, 3, 1, 1, 4, 5)))
print(findExtras("the rain in spain falls mainly in the plains", ('the ',)))

