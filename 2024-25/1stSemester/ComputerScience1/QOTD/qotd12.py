# CS1210: QotD12
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
# Specification: extractVowels(S) takes a string, S, and returns a new
# string containing all of the vowel characters in S, grouped by word.
#
# Example:
#   >>> extractVowels('Seize the day')
#   'eie e a'
#   >>> extractVowels('Midway on our life journey')
#   'ia o ou ie oue'
#
# For full credit, your solution should use a list comprehension; it
# should not use for/while, if/elif/else or assignment.
#
def extractVowels(S):
    return ' '.join([''.join([c for c in word if c in 'aeiouAEIOU']) for word in S.split()])

    #return( ' '.join([c for c in w if c.lower() in 'aeiou' ] for w in S.split() ]))
