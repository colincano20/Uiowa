# CS1210: Lab4 [3 functions to complete]
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
    return(["tberta","cmcano"])

######################################################################
# In this lab, you'll be working on 5 reasonably straightforward short
# functions. None takes more than a single return statement, albeit
# perhaps a statement that has complexity.
#
# Assuming you are working in pairs, compile a single solution file
# that includes both (all three in some cases) of your hawkids in the
# signed() function above. Upload your solution to Gradescope, being
# careful to specify your partner(s) as your "group members" at
# submission time.
#
# MAKE SURE YOU IDENTIFY YOUR LAB PARTNERS IN GRADESCOPE.
#
# For full credit, meet the spec in its entirety, and use only
# concepts introduced in class and in your assigned readings. Pay
# attention to types; return exactly what is being asked for. You will
# not need conditional statements or iteration to solve these
# problems. Each problem pretty much has just a simple one line
# solution that captures the essence of the calculation!
#
######################################################################
# Problem 1
#
# Specification: excise(s1, s2) takes two strings, s1 and s2, and
# returns a new string composed of all the letters in s1 except for
# those that are also in s2. Here, the elements of s2 are all lower
# case, but the case and ordering of elements in s1 are retained in
# the value returned.
#
# Example:
#   >>> excise('The rain in Spain', 'rs')
#   'The ain in pain'
#   >>> excise('falls mainly in the plains...', 'ai')
#   'flls mnly n the plns...'
#
# Use a comprehension.
#
def excise(s1, s2):
    return  ''.join([i for i in s1 if i.lower() not in s2])

# print(excise('The rain in Spain', 'rs'))
# print(excise('falls mainly in the plains...', 'ai'))

######################################################################
# Problem 2
#
# Specification: upcise(s1, s2) takes two strings, s1 and s2, and
# returns a new copy of s1 where all the characters of s1 also in s2
# are converted to upper case, and all the remaining elements of s1
# are converted to lower case. Like in the previous problem, the
# elements of s2 are all lower case, and the ordering within s1 is
# retained in the value returned.
#
# Example:
#   >>> upcise('The rain in Spain', 'rs')
#   'the Rain in Spain'
#   >>> upcise('falls mainly in the plains...', 'ai')
#   'fAlls mAInly In the plAIns...'
#
# Use a comprehension.
#
# Hint: review our discussion of uniqueEnds(S).
#
def upcise(s1, s2):
    return ''.join([((i.lower() in s2.lower()) and i.upper()) or i.lower() for i in s1])

# print(upcise('The rain in Spain', 'rs'))
# print(upcise('falls mainly in the plains...', 'ai'))

######################################################################
# Problem 3
#
# Specification: allWords(S) takes a string, S, and returns the string
# with all numbers replaced by their spelled out equivalent. 
#
# Example:
#   >>> allWords("This is 911 what is your emergency?")
#   'This is nine-one-one what is your emergency?'
#   >>> allWords('7 deadly sins')
#   'seven deadly sins'
#   >>> allWords('Catch-22')
#   'Catch-22'     # 22 unrecognized, does not stand alone
#
# This is a fairly complex problem, so let me give you some
# hints. First, you'll notice that you've been provided a mapping from
# ints to their spelled out equivalent. Second, you will need to write
# two nested comprehensions, one scanning words in S and the "inner"
# comprehension constructing, under appropriate circumstances, the
# spelled out version of a number (review your string methods for
# recognizing "words" in S that are composed of only digits).
#
# Hint: Practice incremental development. Get the basic structure of
# the code so you can reconstruct S after collecting its constituent
# words. Then work on recognizing words that need to change (e.g., by
# turning them to upper case). Then replace turning them to upper case
# with mapping digits to numbers. Get each version right before
# refining it to produce the next version.
#
def allWords(S):
    M={1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
       6:'six', 7:'seven', 8:'eight', 9:'nine', 0:'zero'}
    return ' '.join([(i.isdigit() and '-'.join([M[int(j)] for j in i])) or i for i in S.split()])

# print(allWords("This is 911 what is your emergency?"))
# print(allWords('7 deadly sins'))
# print(allWords('Catch-22'))
