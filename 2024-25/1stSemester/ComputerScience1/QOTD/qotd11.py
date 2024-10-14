# CS1210: QotD11
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
# Specification: countWords(S) takes a string, S, consisting of a
# series of words (alpha characters separated by whitespace
# characters, and returns a dictionary where the keys are lower-case
# versions of the words in S and the values are the number of
# occurrances of the key within S.
#
# Example:
#   >>> countWords('Happy Days')
#   {'happy': 1, 'days': 1}
#   >>> countWords('The rain in Spain')
#   {'the': 1, 'rain': 1, 'spain': 1, 'in': 1}
#   >>> countWords('This is a test of this emergency broadcast system. This is only a test.')
#   {'broadcast': 1, 'only': 1, 'test.': 1, 'is': 2, 'this': 3, 'of': 1, 'system.': 1, 'test': 1, 'emergency': 1, 'a': 2}
#
# Note that the sum of the values in the dictionary will always be the
# total number of words in S.
#>>>[ x:y for x in range(3) for y in range(3) if x != y]
#{0: 2, 1: 2, 2: 1} #keys are unique, order matters
# For full credit, your solution should use a comprehension; it should
# not use for/while, if/elif/else, or assignment. You may of course
# use the appropriate methods of string and list.
#
def countWords(S):
    return({Q: S.lower().split().count(Q) for Q in set(S.lower().split())})
   #


def palindrome(s):
    if len(s)<2:
        return(True)
    elif s[0]!=s[-1]:
        return(False)
    else:
        return(palindrome(s[1:-1]))
#these behave different. How? Recursion forumla is better because it has chance of failing early, instead of finishing the whole amount of charchters.
def palindrome(s):
    return(len(s)<2 or s[0]==s[-1] and palindrome(s[1:-1]))

def palindrome(s):    #racecar==racecar
    return(s == s[::-1])   #::?





def binsearch(L,x):
    def helper(L,x,lo,hi):
        mid = (lo + hi) //2
        if (L[mid] == x):
             return(mid)
        elif (hi-lo <2):
             return(-1)
        elif (L[mid] < x):
             return(helper(L,x,mid,hi))
        else:
            return(helper(L,x,lo,mid))
    return(helper(L,x,0,len(L)))
#we can rewrite this slightly to hide helper function, and share some of the arguements


def seqsearch(L,x)









