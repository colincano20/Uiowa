# CS1210: QotD13
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
# Specification: countVC(S) returns an integer representing the number
# of vowel clusters embedded in the string S. A "vowel cluster" is a
# subsequence of one or more contiguous vowels, with no intervening
# non-vowel letters.
#
# Example:
#   >>> countVC('Amazing grace, how sweet the sound')
#   9
#   >>> countVC('This is a test')
#   4
#   >>> countVC('Master Winnie the Pooh')
#   6
##return( ' '.join([c for c in w if c.lower() in 'aeiou' ] for w in S.split() ]))
# Note that space is not considered a vowel, so spaces between words
# also "reterminate" any vowel clusters; in other words, vowel
# clusters are all contained in a word. You will find the use of if
# and while statements to be useful to solving this problem.

# Think of the problem this way. Scan the characters in S. Each time
# you encounter a vowel, add one to a counter (initially 0) and then
# iterate through all consecutive vowels until you encounter a
# non-vowel. The repeat the whole thing until you run out of
# characters in S: the counter is the number of vowel clusters. So,
# for example:
#     "Amazing grace"
# vc:  1122333333445
#


def countVC(S):
    counter = 0
    for c in range(len(S)):
        if S[c].lower() in 'aeiou':
            if c == 0 or S[c-1].lower() not in 'aeiou':
                counter += 1
            
    return(counter)


#def countVC(S):
#    result = i = 0
#    while i < len(S):
 #       while i < len(S) and S[i].lower() not in 'aeiou':
  #          i = i +1
   #     if i < len(S):
    #        result = result + 1
     #   while i < len(S) and S[i].lower() in 'aeiou':
      #      i = i+1
    #return(result)
