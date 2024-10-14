# CS1210: QotD14
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
# Specficiation: superSum(N) takes a positive integer, N, and returns
# the "super sum" of those digits. The "super sum" is computed by
# repeated addition of the individual digits until a single digit
# result is obtained.
#
# Examples:
#   >>> superSum(5628)
#   3       # 5+6+2+8 = 21; 2+1 = 3
#   >>> superSum(134290)
#   1       # 1+3+4+2+9+0 = 19; 1+9 = 10; 1+0 = 1
#
# Your solution must be recursive, although there are at least two
# equally good ways to approach this problem. However, keep in mind
# that your solution should be strictly recursive, and should not make
# use of any form of iteration.
#

def superSum(N): 
    if N < 10:
        return N
    else:
        i = (sum([int(i) for i in str(N)]))
        return(superSum(i))

# if N<10:
#     return N
# return(superSum(sum([ int(i) for i in list(str(N)) ] )))


# if N<10:
#     return N
# return(superSum(int(str(N)[0] + int(str(N)[1:])))

# if N<10:
#     return N
#  return(superSum(N//10 + N%10))

    
