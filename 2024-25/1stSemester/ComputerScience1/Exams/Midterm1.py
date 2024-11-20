# Python File for Midterm Exam Review

# Directions:
# This script reviews the Midterm 1 exam. Each question is clearly labeled,
# including expressions, answers, explanations, and corrected implementations where applicable.

# Variables from the exam:
T = ("Macky's back", -12, [3, 7, 11], "scarlet billows", {9: "Bush league", 8: 15})
S = "Midway upon the journey of our life, I found myself within a forest dark."
L = [8, "spy boy", ["your", "grandma"], ("iko", "day", "hey", "way"), "fee nane"]
P = {'carter': (39),'reagan': (40),'bush': (41, 43),'clinton': (42),'ford': (38)}

# ---------------------------------------------
# Question 1: Expressions and the Python REPL
# Specification: Evaluate the following expressions.
# ---------------------------------------------

# Question 1.1 (1/1)
expression_1_1 = "5 < P['bush'][0] / 7 < 6"
# My Answer: True
# Correct Answer: True

# Question 1.2
expression_1_2 = "T[1] / len(L[3])"
# My Answer: -1.0
# Correct Answer: -3.0

# Question 1.3
expression_1_3 = "S[36:27:-3] + S[9:11] + S[48:44:-3]"
# My Answer: 'efileourpoesmy'
# Correct Answer: ' f onem'

# Question 1.4
expression_1_4 = "len(S.split()[5]) * str(T[-1][len(S.split()[3]) + 1])"
# My Answer: SyntaxError
# Correct Answer: '151515'

# Question 1.5 (1/1)
expression_1_5 = "T[1] + sum(T[2]) in T[-1]"
# My Answer: True
# Correct Answer: True

# Question 1.6 (1/1)
expression_1_6 = "P[T[-1][9][:4].lower()][1] % L[0]"
# My Answer: 3
# Correct Answer: 3

# Question 1.7
expression_1_7 = "P['reagan'][0] // T[1]"
# My Answer: -3
# Correct Answer: TypeError - Integer cannot be indexed.

# Question 1.8
expression_1_8 = "len('_'.join(L[-2][0:2])) != int(43.2 / 6)"
# My Answer: True
# Correct Answer: False

# Question 1.9
expression_1_9 = "str(T[2][-1]) + str(L[0] / 2)"
# My Answer: 14.0
# Correct Answer: '114.0'

# Question 1.10
expression_1_10 = "(T[4][8] + P['bush'][1]) % 4 / 2"
# My Answer: 16.5
# Correct Answer: 1.0

# ---------------------------------------------
# Question 2: sandwich(S, i, j, U)
# Specification: Implement the function sandwich(S, i, j, U).

# Question 2.1(1/1)
# explain what arguements could cause this solution to fail:
# My Answer: If j is 0, it will fail because threre is no negative zero, so would go from start and not the end

# Question 2.2(0/2)
#If you have indentified a faliure, modify the given solution so that it meets specification
# ---------------------------------------------

def sandwich(S, i, j, U):
    # My Implementation
    return S[:i] + U + (j > 0 and S[-j:])

# Correct Implementation:
def sandwich2(S, i, j, U):
    return S[:i] + U + S[len(S) - j:]

# ---------------------------------------------
# Question 3: uniqueEnd(S) (3/4)
# Specification: Implement a function that checks the unique end of a string.
# ---------------------------------------------

def uniqueEnd(S):
    # My Implementation
    return S[-1] not in S[:-1]

# Correct Implementation:
def uniqueEnd2(S):
    return len(S) > 0 and S[-1] not in S[:-1]

# ---------------------------------------------
# Question 4: subsumes(w1, w2) (1/4)
# Specification: Implement a function to check if one word subsumes another.
# ---------------------------------------------

def subsumes(w1, w2):
    # My Implementation
    return list(w1) in list(w2) or list(w2) in list(w1)

# Correct Implementation:
def subsumes2(w1, w2):
    return set(w1.lower()) <= set(w2.lower()) or set(w2.lower()) < set(w1.lower())

# ---------------------------------------------
# Question 5: vowelRatio(S) (0/4)
# Specification: Calculate the ratio of unique vowels to unique characters in a string.
# ---------------------------------------------

# Specification: Calculate the ratio of vowels to total characters in a string.
    # My Implementaton
def vowelRatio(w):
    vowels = 'a','e','i','o','u'
    unichar = len(list(S))
    return(int(vowels in unichar)/unichar) * 100
  # Correct Implementation
def vowelRatio2(w,alpha='abcdefghijklmnopqrstuvwxyz'):
    return((len(set(w.lower()) & set('aeiou'))*100)//(len(set(w.lower()) & set(alpha))))


# End of Exam Review File
