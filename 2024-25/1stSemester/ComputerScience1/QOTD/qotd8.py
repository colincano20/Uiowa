# CS1210: QotD8
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
# Specification: charCnt(S) takes a string, S, and returns an integer
# representing the number of non-space characters in the string.
#
# Example:
#   >>> charCnt('this is a test')
#   11
#   >>> charCnt('')
#   0
#   >>> charCnt('I love cs1210!')
#   12
#
# One obvious solution involves using string methods to replace spaces
# with empty strings and return the length of the result:
#    def charCnt(S):
#        return(len(S.replace(' ','')))
#
# Here, in order to practice our sequence functions, we're after a
# solution that relies on splitting the string on spaces and adding
# the lengths of the resulting words together. Your solution should
# not use iteration (for or while) but may use the iterative
# constructs discussed in the midterm review (see my 2024-09-23
# posting on Piazza).
#
def charCnt(S):
    return(len(''.join(S.split())))
