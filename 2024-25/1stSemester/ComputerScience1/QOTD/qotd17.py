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
# order. Your function should be iterative, and should not make use of
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
# Your solution should be strictly iterative: make sure you use an
# appropriate iterative form. Feel free to allow your function to
# modify L1 and L2.
#
def merge(L1, L2):
    result = []
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    while L1 and L2:
        if L1[0] <= L2[0]:
            result.append(L1[0])
            L1.pop(0)
        elif L1[0] >= L2[0]:
            result.append(L2[0])
            L2.pop(0)
    if len(L1) == 0:
        result.extend(L2)
    if len(L2) == 0:
        result.extend(L1)
        
    return result



def merge1(L1,L2):
    result = []
    while L1 and L2:
        if L1[0] < L2[0]:
            result.append(L1.pop(0))
        else:
            result.append(L2.pop(0))
        return(result + L1 + L2)

print(merge([1, 3, 5],[2, 4, 6]))
print(merge([1, 3, 4, 5],[2, 4, 6, 8]))
print(merge([1, 2, 3], []))
print(merge([-1,-0.5,0,5,8,99], [69,999]))
