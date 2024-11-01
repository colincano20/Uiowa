# CS1210: Lab6 [4 functions to complete]
######################################################################
# READ ALL INSTRUCTIONS CAREFULLY.
#
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partner(s), and
#  2) you have not shared it nor will share it with anyone else.
#
# ToDo: Change the two "hawkid" strings to match the hawkids of you
# and your partner(s). Your hawkid is the "login identifier" that you
# use to login to all University services: it is not your email
# address or your student id number.
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "segre". 
#
# Note: if there are 3 of you, add a third string to the list returned
# by signed() below (e.g., change ["hawkid1","hawkid2"] to
# ["hawkid1","hawkid2","hawkid3"], using your own three UI login
# identifiers as the hawkid values).
#
def signed():
    return(["cmcano","cyoung21"])

######################################################################
# Specification: np(S) takes a lower case string, S, and returns True
# if S is a "near palindrome", and False otherwise.
#
# A "near palindrome" is a string that reads the same forwards or
# backwards when it is off by one. In other words, there is an extra
# letter that you ignore at either the beginning or the end of S, but
# not both.
#
# Examples:
#   >>> np('ailipilia')
#   False		# a palindrome
#   >>> np('ailipilias')
#   True		# ignore final 's'
#   >>> np('pailipilia')
#   True		# ignore initial 'p'
#   >>> np('ailipixlia')
#   False		# not a near palindrome
#def palindrome(s):
    #return(len(s)<2 or s[0]==s[-1] and palindrome(s[1:-1]))
# You are free to use any approach you like, although one suggestion
# might be to use slices.
#
def np(S):
    return (S[1:] == S[1:][::-1]) or (S[:-1] == S[:-1][::-1])


######################################################################
# Specification: iqp(S) takes a lower case string, S, and returns True
# if S is a "quasi palindrome", and False otherwise.
#
# A "quasi palindrome" is like a "near palindrome" except you can skip
# up to one letter anywhere in the string -- not just at the beginning
# or the end of S! So:
#
# Examples:
#   >>> iqp('ailipilia')
#   True		# a palindrome
#   >>> iqp('ailipilias')
#   True		# ignore final 's'
#   >>> iqp('pailipilia')
#   True		# ignore initial 'p'
#   >>> iqp('ailipixlia')
#   True		# a quasi palindrome, ignore 'x'
#   >>> iqp('aixlipilixa')
#   False               # 2 deviations...
#
# Your function should use iteration; feel free to make use of np()
# defined above.
#
# Hint: work your way inwards, trimming away matching ends. If and
# when you get the first mismatch, defer to np() which allows one and
# only one mismatch.
#
def iqp(S):
    for i in range(len(S)//2):
        if S[i] != S[len(S) - i -1]:
            return(np(S[i:len(S)-i]))
    return(True)

        
  


######################################################################
# Specification: rqp(S) takes a lower case string, S, and returns True
# if S is a "quasi palindrome", and False otherwise.
#
# This is just a recursive rewrite of iqp(). Again, feel free to use
# np() defined above.
#
def rqp(S):
    if S[0] != S[-1] or len(S) < 2:
        return np(S)
    return rqp(S[1:-1])

print(rqp('ailipixlia'))
print(rqp('ailipilia'))

######################################################################
# Specification: cntDiff(S1, S2) takes two strings, S1 and S2, and
# returns an integer number of case-independent character differences
# between the two strings.
#
# Examples:
#   >>> cntDiff('Eagle', 'eagle')  
#   0         # case doesn't matter
#   >>> cntDiff('Eagles', 'eagle')
#   1         # extra 's'
#   >>> cntDiff('expressions', 'express')
#   4         # extra 'ions'
#   >>> cntDiff('expertise', 'experts')
#   2         # extra 'i' and 'e'
#
# Your function should be recursive.
#
# To formulate your solution, consider peeling back characters that
# agree from the left end of both words. When you exhaust one sequence
# but not the other, add in the length of the remaining
# sequence. Otherwise, when the characters diverge, add 1 or 2 to the
# minimum number of differences found between the remaining "tails" of
# the sequences. Be sure to consider (a) ignoring a character of the
# remaining first sequence, (b) ignoring a character of the remaining
# second sequence, or (c) ignoring the first character of both
# remaining sequences.
#
def cntDiff(S1, S2):
    if len(S1) == 0:
        return(len(S2))
    elif len(S2) ==0:
        return(len(S1))
    elif S1[0].lower() == S2[0].lower():
        return(cntDiff(S1[1:], S2[1:]))
    return(1+min(cntDiff(S1[1:], S2[1:]), cntDiff(S1, S2[1:]), cntDiff(S1[1:], S2[1:])))

