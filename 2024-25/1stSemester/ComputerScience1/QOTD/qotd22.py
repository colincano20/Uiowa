# CS1210: QotD22
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
# Specification: euclid(x, y) takes two positive integers and returns
# their greatest common divisor, or gcd. The gcd is the largest
# integer 1<=i<=min(x, y) that evenly divides both x and y.
#
# Your solution should be based on Euclid's algorithm, due Euclid of
# Alexandria, the famous ancient Greek mathematician credited with the
# development of Euclidean geometry (est. 330BC-270BC).  Euclid's
# algorithm computes the remainder r obtained by dividing the larger
# of x,y by the smaller of x,y. If r is 0, then the divisor is the
# gcd; otherwise, repeat the process using r and the smaller of x,y.
#
# Your solution should be recursive.
#
def euclid(x, y):
    if x > y:
        if x % y == 0:
            return y
        else:
            return(euclid(y,(x%y)))
    else:
        return(euclid(y,x))
print(euclid(270,192))

def euclid2(x,y):

    r = max(x,y) % min(x,y)
    if r == 0:
        return(min(x,y))
    return(euclid2(r,min(x,y)))
    
print(euclid2(270,192))


