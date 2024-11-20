# CS1210: Lab12 [2 functions to complete]
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
    return(["cmcano","trwahlstrom"])

######################################################################
# The powerset of a set S is the set of all sets that are subsumed by
# S. So, for example, if S={1, 2, 3}, then powersetR(S)={{1, 2, 3}, {1,
# 2}, {1, 3}, {2, 3}, {1}, {2}, {3}, {}}. If S has 4 elements, the
# powersetR(S) will have 16 elements, including S and the empty set.
#
# Specification: write a function powersetR(S) which takes a set, S,
# and returns a set of tuples representing all of the sets that are
# subsumed by the original set S.
#
# Your function should be recursive.
#
# Example:
#   >>> powersetR(set(()))
#   {()}   # The empty set is in every other set, including itself
#   >>> powersetR(set({1}))
#   {(1,), ()}
#   >>> powersetR({1, 2})
#   {(1,), (1, 2), (2,), ()}
#   >>> powersetR({1, 2, 3})
#   {(1, 2), (2,), (1, 2, 3), (2, 3), (1,), (3,), (), (1, 3)}
#
# Why tuples? Because like lists, sets are mutable, and are therefore
# not hashable and cannot themselves be used as elements of a
# set. Here, we choose to convert all of the elements of the powerset
# of S into tuples, which are immutable and hashable, and can
# therefore be used as elements of a set.
#
def powersetR(S):
    if len(S) == 0:
        return {()}
    element = S.pop()
    tempset = powersetR(S)

    powerset = set(tempset)
    for sub in tempset:
        powerset.add(sub + (element,))
    return powerset


######################################################################
# Specification: write a function powersetI(S) which takes a set, S,
# and returns a set of tuples representing all of the sets that are
# subsumed by the original set S.
#
# This is the same as the solution you just provided, but it should be
# iterative. This solution takes advantage of the observation that if
# S has k elements, the powerset of S will have exactly 2^k elements.
#
# Because there are exactly 2^k k-element combinations of {0, 1}, we
# can let each such combination correspond to an element in the
# powerset of S in the following way. The powerset of a set with k
# elements can be formed by considering all combinations of k bits,
# where a 1 in position i (where 0<=i<k) indicates that the ith
# element of S is included in this element of the powerset, and a 0 in
# that position indicates that the ith element of S is not included in
# this element of the powerset.
#
# Knowing that the built-in Python function bin(i) returns the binary
# represention of the number i as a string (expressed as '0b' followed
# by k 0's or 1's), use this information in a counting loop from 0 to
# 2^k-1 to generate each element of the powerset.
#
# Example:
#   >>> powersetI({1, 2, 3})
#   {(), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3)}
# with corresponding bit strings (one of several mappings):
#   {'0b000', '0b001', '0b010', '0b011', '0b100', '0b101', '0b110', '0b111'}
#
def powersetI(S):
    powerset = set()
    for i in range(2**len(list(S))):
        powerset.add(tuple(list(S)[j] for j in range(len(list(S))) if (i & (2**j)) != 0))
    return powerset
