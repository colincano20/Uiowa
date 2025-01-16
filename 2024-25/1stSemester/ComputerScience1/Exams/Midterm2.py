# Python File for Midterm Exam Review

# Directions:
# This script reviews the Midterm 2 exam. Each question is clearly labeled,
# including explanations, answers, and corrections where applicable.

# ---------------------------------------------
# Question 1: countExtras(S) (1/5)
# Specification: Count elements in a sequence that are "extra" based on a condition.
# ---------------------------------------------

def countExtras(S):
    # My Implementation
    return len([x for x in S for y in y if x == y])

# Correct Implementation:
def countExtras2(S):
    return(len(S) - len(set(S)))
#print(countExtras2((1,2,3,1,1,4,5)))
# Explanation:
# Your logic was on the right track but had a syntax or minor logic error. 
# The corrected version iterates and counts efficiently using `sum()`.

# ---------------------------------------------
# Question 2: countPeaks(S) (5.5/6)
# Specification: Count peaks in a sequence (elements greater than their neighbors).
# ---------------------------------------------
# Question 2.1 (4.5/5)

# My Implementation
def countPeaks(S): 
    count = 0
    for i in range(len(S) - 1):
        if S[i] > S[i-1] and S[i] > S[i+1]:
            count += 1
        if S[-1] >= S[-2] and S[-1] > S[0]:
            count += 1
    return count

# Correct Implementation:
def countPeaks2(S):
    count = 0
    for i in range(len(S)):
        if S[i-1] <= S[i] > S[(i+1)% len(S)]:
            count += 1
    return count

# Question 2.2 (1/1): 
# Specification: Assuming S has N elements, what is the runtime of your solution?
# Anwser: O(N)

# ---------------------------------------------
# Question 3: stringify(S, c='.') (3/7)
# Specification: Convert a nested sequence into a string with a given separator.
# ---------------------------------------------
# My Implementation
def stringify(S, c='.'):
    result = []
    for i in S:
        for j in S:
            if type(i) == int or str or float:
                result.append(i)
            else:
                result.append(''.join(j))
    return(c.join(result))

# Correct Implementation:
def stringify2(S, c='.'):
    if isinstance(S,(list,tuple,set,range)):
        return c.join([stringify2(x,c) for x in S if x or x == 0])
    return(str(S))

# Explanation:
# - Your version didn't handle recursion into nested structures perfectly.
# - The corrected version uses `join` for cleaner concatenation.

# ---------------------------------------------
# Question 4: findExtras(S, skip=()) (1.5/7)
# Specification: Find "extra" elements in a sequence while skipping specific values.
# ---------------------------------------------
# Question 4.1 (0/5)
def findExtras(S, skip=()):
    S = S.split()
    new = []
    if len(S) <= 1:
        return None
    if S[0] == skip:
        S.pop(S[0])
    if S[0] in S[1:]:
        new.append(S[0])
    else:
        S.pop(S[0])
    return(findExtras(S[1:], set(new)))

# Correct Implementation:
def findExtras2(S, skip=()):
    if len(S) == 0:
        return(set())
    if S[0] not in skip and S[0] in S[1:]:
        return({S[0]} | findExtras2(S[1:], skip))
    return(findExtras2(S[1:], skip))

# Question 4.2: Why is using tuples a smart choice?(0.5/1):
# Anwser: Lists are mutable

# Question 4.3: Runtime Complexity (1/1)
# Your Answer: O(N^2)
# Correct Answer: O(N^2)

