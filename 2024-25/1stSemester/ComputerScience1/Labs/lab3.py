# CS1210: Lab3 [4ish functions to complete]
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
    return(["hawkid1","hawkid2"])

######################################################################
# In this lab, you'll be working on 5 reasonably straightforward short
# functions. None takes more than a single return statement, albeit
# perhaps a statement that has complexity.
#
# Assuming you are working in pairs, compile a single solution file
# that includes both (all three in some cases) of your hawkids in the
# signed() function above. Upload your solution to Gradescope, being
# careful to specify your partner(s) as your "group members" at
# submission time.
#
# MAKE SURE YOU IDENTIFY YOUR LAB PARTNERS IN GRADESCOPE.
#
# For full credit, meet the spec in its entirety, and use only
# concepts introduced in class and in your assigned readings. Pay
# attention to types; return exactly what is being asked for. You will
# not need conditional statements or iteration to solve these
# problems. Each problem pretty much has just a simple one line
# solution that captures the essence of the calculation!
#
######################################################################
# Problem 1
#
# Specification: chainIf(s1, s2) takes two strings, s1 and s2, and
# returns the concatenation of s1 and s2 if s1 is not in s2, otherwise
# it simply returns s1.
#
# Example:
#   >>> chainIf('plan','planning')
#   'plan'
#   >>> chainIf('not', 'ANGRY')
#   'notANGRY'
#
# Note: Be concise: your solution should not use an if statement.
#
def chainIf(s1, s2):
    pass

######################################################################
# Problem 2
#
# Specification: skipZip(L, i) takes a list, L, and an integer, i,
# where 0 <= i < len(L) and alters the list L by setting every other
# element of L, starting with index i, to 0. The function does not
# return a value.
#
# Examples:
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> skipZip(L, 7)
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 0, 8, 0]
#   >>> skipZip(L, 1)
#   >>> L
#   [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]
#
def skipZip(L, i):
    pass

######################################################################
# Problem 3
#
# Specification: skipZipLtd(L, i, j, k) extends skipZip(L, i) to limit
# the replacement of elements to those elements in L between i and j
# with stepsize k.
#
# Examples:
#
def skipZipLtd(L, i, j, k):
    pass

######################################################################
# Problems 4
#
# Specification: skipFlip(L, i, j, k) is analagous to skipZipLtr(L, i,
# j, k) but instead of zeroing out elements of L, simply inverts their
# sign.
#
# Examples:
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> skipFlip(L, 2, 9, 3)
#   >>> L
#   [0, 1, -2, 3, 4, -5, 6, 7, -8, 9]
#
# Your solution should make use of a specific Python function,
# map(). Map is a sequence function, much like sum(), min(), max(),
# any() and all() which, unfortunately, is not covered in your
# textbook. map() takes at least two arguments, a function of one
# argument (by name) and a sequence (like a list) and returns an
# iterator -- something much like range() but more flexible. If the
# function passed happens to mutate the sequence (here, a list), then
# map() can also be used to modify elements of a list in a flexible
# fashion.
#
# Here's an example of the use of map():
#   >>> X = ((1, 2, 3), [5, 6, 7], [-2, -2])
#   >>> sum(map(max, X))
#   8
# In this example, map() applies max() to each of the elements of X,
# which we then sum together.
#
# Your solution has two parts. The first is easy: write a function
# negate(n) that takes a number as its only argument and returns the
# negation of that number. This function will be used as a "helper"
# function in your skipFlip solution, a topic will discuss later in
# class.
#
def negate(n):
    pass

# The second part of your solution is the skipFlip(L, i, j, k)
# part. Here, you should in part be inspired by skipZipLtd(L, i, j,
# k), but you will also use map(negate, ____ ) to modify L.
#
def skipFlip(L, i, j, k):
    pass
