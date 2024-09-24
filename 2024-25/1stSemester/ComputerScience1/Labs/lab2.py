# CS1210: Lab2 [5 functions to complete]
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
    return(["cmcano","janczak"])

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
# Specification: theSame(S1, S2) takes two sequences, S1 and S2, and
# returns True if the elements of S1 and the elements of S2 are the
# same (it returns False otherwise).
#
# Examples:
#   >>> theSame('abcde', ['c', 'b', 'a', 'a', 'e', 'd', 'a'])
#   True
#   >>> theSame('abc', 'cde')
#   False
#   >>> theSame(range(3), (2, 1, 2, 1, 1, 0))
#   True
#
# Note that sequences S1 and S2 needn't be of the same type.
#
def theSame(S1, S2):
    return(set(S1) == set(S2))

######################################################################
# Problem 2
#
# Specification: inNeither(S1, S2) takes two sequences, S1 and S2, and
# returns a set containing all of the elements of either that occur in
# just one of the two sequences.
#
# Examples:
#   >>> inNeither(range(4), range(2, 7))
#   {0, 1, 4, 5, 6}
#   >>> inNeither('abc', 'cde')
#   {'e', 'a', 'd', 'b'}
#
def inNeither(S1, S2):
    return(set(S1) ^ set(S2))

######################################################################
# Problem 3
#
# Specification: multTail(S, i, j) takes a sequence, S, an integer 0
# <= i < len(S) and a second integer j, and returns a (new) sequence
# consisting of S with its last i characters repeated exactly j times.
#
# Examples:
#   >>> multTail([1, 2, 3], 2, 2)
#   [1, 2, 3, 2, 3]
#   >>> multTail((1, 3, 5, 6), 2, 3)
#   (1, 3, 5, 6, 5, 6, 5, 6)
#   >>> multTail("scissors", 4, 0)
#   'scis'
#   >>> multTail('neutral', 3, 1)
#   'neutral'
#
# Hint: Careful! Consider edge cases carefully!
#
def multTail(S, i, j):
    return(S[:-i] + j*S[-i:])

######################################################################
# Problem 4
#
# Specification: multCenter(S, i, j) takes a sequence, S, an integer i
# <= len(S) and an integer j, and returns a new sequence that is
# identical to the sequence S but with the centermost i elements of S
# replicated j times.
#
# Note: "centermost" may not be exact if S is of odd length and i is
# even (or if S is of even length and i is odd). In such cases,
# "centermost" should shift towards the beginning of the sequence (see
# first and third examples below).
#
# Example:
#   >>> multCenter((1, 2, 3, 4, 5, 6), 1, 3)
#   (1, 2, 3, 3, 3, 4, 5, 6)
#   >>> multCenter((1, 2, 3, 4, 5, 6), 2, 2)
#   (1, 2, 3, 4, 3, 4, 5, 6)
#   >>> multCenter("abcdefghi", 4, 2)
#   'abcdefcdefghi'
#   >>> multCenter((1, 2, 3, 4, 5, 6), 2, 0)
#   (1, 2, 5, 6)
#
# Hint: the shift is suggestive of integer division.
#
# Note: Again, the solution consists of a single statement; iteration
# is unncessary and should not be used.
#
def multCenter(S, i, j):
    return((S[:((len(S)-i) // 2)]) +  j*S[((len(S)-i) // 2): (len(S) + i) // 2] + S[(len(S) + i) // 2:])

######################################################################
# Problem 5
#
# Specification: distribute(S) takes a sequence of integers and
# returns a list of len(S) elements evenly distributing sum(S) across
# these elements, with larger elements occurring at the end of the
# result.
#
# Examples:
#   >>> distribute(range(9))
#   [4, 4, 4, 4, 4, 4, 4, 4, 4]
#   >>> distribute((2, 3, 5, 1))
#   [2, 3, 3, 3]
#   >>> distribute(range(4, 14))
#   [8, 8, 8, 8, 8, 9, 9, 9, 9, 9]
#
# Hint: my solution employs sum(), integer division and sequence
# multiplication).
#
def distribute(S):
    return ((len(S)*[sum(S)// len(S)]) + [sum(S) % len(S)])
