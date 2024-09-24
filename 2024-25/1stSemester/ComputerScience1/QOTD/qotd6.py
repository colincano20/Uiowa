# CS1210: QotD6
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["cmcano"])

######################################################################
# Specification: validate(S) takes a sequence, S, with at least two
# elements and returns True if and only if the first and last
# characters of S appear in order.
#
# Example:
#   >>> validate('false')
#   False           # because f follows e
#   >>> validate('False')
#   True            # because F comes before e
#   >>> validate('suspects')
#   True            # because s and s are in order
#
# Note: you don't need iteration (for/while) or conditionals (if/else)
# to solve this problem.
#
def validate(S):
   return(S[0] <= S[-1])
