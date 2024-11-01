D={'that':6, 'to':4, 'be':5, 'the':8, 'or':2, 'not':3, 'question':9, 'is':7}
L=['taken','surprise','over','come','by']
M=[(1, 2), True, [3, 4, 5], "Hamlet", False]
S='coffee coke tea lemonade milk sprite'
T=('False', (13, 12), "my name is", ("Abraham", "Lincoln"), {'x':-2, 7:'x', 'z':2})
U="Standing at the crossroads trying to read the sign"
# Specification: nearAnagram(S1, S2) takes two sequences, S1 and S2,
# and returns True if the two sequences are possible anagrams of each
# other.
#
# Recall an anagram is simply a permutation of the characters of one
# string to make another word, such as "servant" and "taverns" (here,
# we’ll extend the notion from strings to sequences, including lists
# and tuples).
#
# A "near anagram" are two sequences that share the same length and
# are made of identical elements, but may differ in how many times
# each element occurs.
#
# Example:
# >>> nearAnagram(’taverns’, ’servant’)
# True
# >>> nearAnagram([1, 2, 3, 1], (2, 2, 1, 3))
# True
# >>> nearAnagram([1, 2, 3, 1], [3, 2, 1])
# False
#
# Note: do not use assignment or conditionals.
#
def nearAnagram(S1, S2):
    return(set(S1) == set(S2) and len(S1)== len(S2))

#return(len(S1)==len(S2) and set(S1)==set(S2))


#Specification: antigram(S1, S2) takes two sequences, S1 and S2, and
# returns True if the two sequences have identical length, identical
# first and last elements, but share no other elements.
#
# Example:
# >>> antigram(’taverns’, ’servant’)
# False
# >>> antigram([1, 2, 3, 1], (1, 7, 4, 1))
# True
# >>> antigram([1, 2, 3, 7, 1], [1, 8, 3, 5, 1])
# False
#
def antigram(S1,S2):
   return(len(S1)==len(S2) and S1[0]==S2[0] and S1[-1]==S2[-1] and not set(S1[1:-1]) & set(S2[1:-1]))


# Specification: invert(L) takes a list L and modifies it by
# exchanging its first and last halves while also reversing the last
# (now first) half. The function should not return any value.
# L=list(range(12))
# >>> invert(L)
# >>> L
# [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
# >>> L=[]
# >>> invert(L)
# >>> L
# []
# >>> L=[1, 2]
# >>> invert(L)
# >>> L
# [2, 1]
# Hint: no iteration.
#
# Hint: list operations must be destructive.
#
def invert(L):
    L[:len(L)//2],L[len(L)//2:] = L[len(L)//2:-1], L[:len(L) //2]










# Specification: Write a function reverseInt(n) that takes a positive
# integer n and returns the integer that has the same digits of n
# but in reverse order.
#
# Example:
# >>> reverseInt(7102)
# 2017
# >>> reverseInt(1024)
# 4201
# >>> reverseInt(100)
# 1
# >>> reverseInt(5255498)
# 8945525
#
# Hint: it’s OK if leading zeros disappear
#
def reverseInt(n):
    return(int(str(n)[::-1]))


######################################################################
# Specification: write a function palindrome(S) that returns True if and
# only if the sequence S is composed of a subsequence followed by a
# reversed copy of the same subsequence, with an optional separating
# element only in the event len(S) is odd.
#
# Examples:
# >>> palindrome([1, 2, 3, 4, 3, 2, 1])
# True
# >>> palindrome(’racecar’)
# True
# >>> palindrome((3, 5, 3, 5))
# False
#
# Note that both the null sequence and sequences of length 1 are
# palindromes.
#
def palindrome(S):
    return(str(S)[0:] == S[-1:])





# Specification: write a function collapse(L) that takes a nonempty
# list of non-negative integers, L, and modifies the list by removing
# its first k elements, where k is the smallest value in the list. The
# function should not return a value (i.e., it should return None).
#
# Examples
# >>> x=[4, 5, 3, 6, 7]
# >>> collapse(x)
# >>> x
# [6, 7]
# >>> collapse(x)
# >>> x
# []
#
def collapse(L):
    #k = min(L)
    #del L[:k]
    L[:min(L)]=[]
#remove first k amount of numbers in list


#Specification: write a function sumDigits(n) that takes as input an
# integer, n, and returns the sum of the digits of n while respecting
# the sign of n. Your solution should be elegant and concise!
#
# Note: no for/while required; reviewing [PE] C8 is a good idea.
#
# Example:
# >>> sumDigits(-132248)
# -20
# >>> sumDigits(101)
# 2
# >>> sumDigits(0)
# 0
# >>> sumDigits(78214905)
# 36
#
# Careful: this one does require the use of a conditional expression,
# which we have yet to cover in class, so technically this one would
# not appear on the exam!
#
def sumDigits(n):
    pass







