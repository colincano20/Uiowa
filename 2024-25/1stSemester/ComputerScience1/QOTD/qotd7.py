# CS1210: QotD7
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
# Specification: flatCenter(L, k) takes a list, L, of length >= 1 and
# a nonnegative integer k and modifies L by replacing the single
# centermost element of L with k 0's. Note that this function does not
# returns a value, but rather destructively modifies the input list.
#
# Examples
#   >>> X=list(range(6))    # assignment yields no value
#   >>> X		    # X is a list of 7 elements
#   [0, 1, 2, 3, 4, 5, 6]
#   >>> flatCenter(X, 4)    # flatCenter() yields no value
#   >>> X		    # value of X has changed!
#   [0, 1, 2, 0, 0, 0, 0, 4, 5]
#   >>> flatCenter(X, 0)    # one more round
#   >>> X
#   [0, 1, 2, 0, 0, 0, 4, 5]  # one shorter!
#
# The key to this function is the fact that lists are mutable!
#
# So even if we return no value, flatCenter() can change its world
# through the "side effect" of mutating or modifying the list it was
# given, X, which flatCenter() calls L internally.
#
def flatCenter(L, k):
    L[len(L) // 2: (len(L) // 2)+ 1] = [0] * k

