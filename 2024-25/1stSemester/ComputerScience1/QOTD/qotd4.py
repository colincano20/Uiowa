# CS1210: QotD4
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
# Specification: sandwich(S, i, j, U) takes two sequences, S and U,
# and two non-negative integers i and j, and returns a new sequence where the
# elements of U appear sandwiched in between the first i elements and
# the last j elements of S. 
#
# Example:
#   >>> sandwich('abcdefg', 2, 4, 'ZZZ')
#   'abZZZdefg'
#   >>> sandwich(tuple(range(1, 16, 2)), 3, 2, tuple(range(100, 102)))
#   (1, 3, 5, 100, 101, 13, 15)
#   >>> sandwich('abcd', 0, 5, 'Z')
#   'Zabcd'
#
# Your code must work for strings, tuples and lists. Strive for a
# concise solution. You don't need conditionals, loops, or any other
# construct we haven't explicitly covered in class. Be careful when i
# or j exceed the length of S (see the example given).
#
def sandwich(S, i, j, U):
    return(S[:i] + U + S[-j:])
# return(S[:i] + U + S[len(S)-j:])  ensures -0 works properly, yet not perfect 10-15 is -5 compared to whole thing
# return(S[:i] + U + S[max(0,len(S)-j:]) wow....  
    
   






