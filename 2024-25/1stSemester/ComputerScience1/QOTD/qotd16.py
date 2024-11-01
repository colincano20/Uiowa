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
# Specification: Write a function findPair(S, target) where S is a
# sequence of integers (sorted) and target is an integer, where
# findPair(S, target) returns (i, j) if two elements of S sum to
# target, else it returns False.
#
# Example:
#  >>> S=[2, 9, 13, 16, 23, 24, 30, 35, 37, 44, 46, 51, 58, 65, 72]
#  >>> findPair(S, 90)
#  (9, 10)
#
# The general idea is to use two separate indexes, i and j, to scan S
# and compare S[i]+S[j] against target. If the sum is correct,
# findPair() should return (i, j). If no solution is found, it should
# simply return False.
#
# There are several approaches, where the simplest lets i range over
# elements of S and j range, independently, over the elements of S.
#
# But if you think about it, comparing all combinations of i, j is
# wasteful, because you'll compare both S[1]+S[3] and S[3]+S[1] to
# target. If one won't work, the other won't either! So the trick here
# is to find some way of minimizing the comparisons you make so that
# you don't do any redundant work. Hint: remember, the sequence is
# sorted, so you can work with that.
#
# You can use any approach you like here: iterative, recursive, its
# entirely up to you.
#
def findPair(S, target):
    i = 0
    j = len(S) - 1
    while i < j:
        if S[i] + S[j] == target:
            return (i, j)
        elif S[i] + S[j] > target:
            j -= 1  
        else:
            i += 1  
    return False  

    


# solution
def findPair(S, target):
    for in in range(len(S)):
        for j in range(len(S)):
            if S[i] + S[j] == target and i != j:
                return(i,j)
    return False


#efficient
def findPair(S, target):
    for in in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] + S[j] == target:
                return(i,j)
    return False



#we can do better, S is in order, once S[i] + S[j] exceeds the target, we stop looking and increment i

def findPair(S, target):
    for i in range(len(S)):
        j= i +1
        while (j<len(S) and S[i] + S[j] <= target):
            if S[i] + S[j] == target:
                return(i,j)
            j = j +1
    return False




#the idea is to count how many basic operations we make in the course of solving a partiuclar problem.
# Here, we will assume the basic operation is the comparison of S[i] + S[j]

def findPair0(S, target, count = 0):  #loser
    for i in range(len(S)):
        for j in range(len(S)):
            count = count + 1
            if S[i] + S[j] == target:
                return(i,j,count)
    return((False,count))



def findPair1(S, target,count = 0):
    for in in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] + S[j] == target:
                return(i,j,count)
    return ((False,count))


def findPair2(S, target, count=0):    #winner
    for i in range(len(S)):
        j= i +1
        while (j<len(S) and S[i] + S[j] <= target):
            count = count + 2
            if S[i] + S[j] == target:
                return(i,j,count)
            j = j +1
    return ((False,count))
