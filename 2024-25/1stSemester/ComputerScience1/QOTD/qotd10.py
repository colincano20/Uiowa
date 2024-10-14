# CS1210: QotD10
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
# Specification: smooth(L, k) takes a list of numeric values (int or
# float) and a smoothing parameter, k, where 1 <= k < len(L), and
# returns a new list that contains a "smoothed" version of the values
# in L.
#
# Each "smoothed" value in the result consists of the mean of k
# elements in the original list, L, starting with the corresponding
# index as the result. So:
#    >>> smooth([3, 5, 4, 7, 2, 8], 2)
#    [4.0, 4.5, 5.5, 4.5, 5.0]
# computed as follows:
#    [((3+5)/2), ((5+4)/2), ((4+7)/2), ((7+2)/2), ((2+8)/2)]
# Note that the length of the result will always be k-1 elements
# shorter than L.
#
# For full credit, your solution should use a comprehension; it
# should not use for/while, if/elif/else, or assignment.
#
def smooth(L, k):
   return ([sum(L[i:i+k]) / k for i in range(len(L) - k + 1)])
   #

