# CS1210: QotD15
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
# Specification: findIt(L, x) takes a possibly nested list L of
# elements and a target element x and returns True if x is found
# in L, and False otherwise.
#
# Example:
#   >>> findIt([1, 4, [2, [18, 3], -1, -9]], 18)
#   True
#   >>> findIt([1, 4, [2, [18, 3], -1, -9]], [18, 3])
#   True
#   >>> findIt([1, 4, [2, [18, 3], -1, -9]], [])
#   False
#   >>> findIt([1, 4, [2, [], -1, -9]], [])
#   True
#
# Your solution must be purely recursive; it should not use for, while
# or any sort of comprehension. Pay special attention to the last two
# cases above, as producing this behavior requires some thought.
#
# Note: normally, in Python, [] is in any list, but, here, only
# explicit [] is recognized (see last two examples above).
#
# Be prepared to spend some time on this one. It's quite challenging,
# even though the solution is, in the end, straightforward. To help
# find the solution, you might want to add a few print statements to
# reveal the arguments on each recursive invocation.
#

#Base Case - Check if List is Empty:

#If the list L is empty, return whether x is the empty list []. This will handle cases like the example findIt([], []).
#Iterate Over Elements of the List:


def findIt(L, x):
    if len(L) == 0:
        return x == []
    if L[0] == x:
        return True
    return findIt(L[1:], x)
    
 
    

# x needs to be found within L, potenially nested list


#notpurely recursive
#def findIt(L.x):
#    if L == x:
 #       return True
 #   elif not isinstance(L,list):
 #       return(False)
#    return(any([findIt(e,x) for e in L]))




# this one fails one of the tests case!

#    if L == x:
#       return True
#    elif not isinstance(L,list) or L ==[]:
#       return(False)
#   return(findIt(L[0],x) or findIt(L[1:], x))




#solution

def findIt(L,x):
    if isinstance(L,list) and len(L) > 0: #censor tail
        return(L[0] == x or findIt(L[0],x) or findIt(L[1:],x))
    return False



print(findIt([1, 4, [2, [18, 3], -1, -9]], 18))
print(findIt([1, 4, [2, [18, 3], -1, -9]], [18, 3]))
print(findIt([1, 4, [2, [18, 3], -1, -9]], []))
print(findIt([1, 4, [2, [], -1, -9]], []))
print(findIt([],[]))


