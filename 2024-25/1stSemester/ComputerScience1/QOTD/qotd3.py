# CS1210: QotD3
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
# Specification: multDiff(i, j) takes two integers, i and j, and
# returns the the product of i and j less the sum of i and j.
#
# Example:
#   >>> multDiff(2, 3)
#   1
#   >>> multDiff(2, -3)
#   -5
#
def multDiff(i, j):
    anwser =(i * j)-(i +j)
    return(anwser)
