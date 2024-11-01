# CS1210: QotD16
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
# Specification: Write a function merge(L1, L2) where L1 and L2 are
# lists of numbers in sorted order; your function should return a new
# list containing all of the elements in L1 and L2 still in
# order. Your function should be recursive, and should not make use of
# any form of sort.
#
# Example:
#   >>> merge([1, 3, 5],[2, 4, 6])
#   [1, 2, 3, 4, 5, 6]
#   >>> merge([1, 3, 4, 5],[2, 4, 6, 8])
#   [1, 2, 3, 4, 4, 5, 6, 8]
#   >>> merge([1, 2, 3], [])
#   [1, 2, 3]
#
# Hint: imagine constructing your new list by repeatedly removing the
# smaller between L1 and L2 and adding it to the list.
#
# Your solution should be strictly recursive: no iteration is
# necessary.
#
def merge(L1, L2):
    result = []
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    if L1[0] <= L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    else:
        return [L2[0]] + merge(L1, L2[1:])

print(merge([1, 3, 5],[2, 4, 6]))
print(merge([1, 3, 4, 5],[2, 4, 6, 8]))
print(merge([1, 2, 3], []))
        
