# CS1210: QotD5
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

# Specification: cleave(S1, S2, i) takes two sequences, S1 and S2,
# which must be either tuples or strings, and a non-negative integer,
# i and returns a tuple of two sequences formed by cleaving S1 and S2
# at location i and splicing each sequence head with the other
# sequence's tail.
#
# Example: 
#   >>> cleave('computer', 'science', 3)
#   ('comence', 'sciputer')
#   >>> cleave((1, 2, 3), (4, 5, 6, 7), 2)
#   ((4, 5, 3), (1, 2, 6, 7))
#
# Note: you don't need iteration (for/while) or conditionals (if/else)
# to solve this problem.
#
# Note: the Autograder is configured to ignore ordering within the
# result, so the ('comence', 'sciputer') and ('sciputer', 'comence')
# are equally correct.
#
def cleave(S1, S2, i):
    return((S1[:i] + S2[i:]), (S2[:i] + S1[i:]))
