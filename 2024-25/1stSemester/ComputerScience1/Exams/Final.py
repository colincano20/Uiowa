"""
Question 1: smooth(L, k)
Points: 3 / 4

Specifications:
- Modify the input list L by replacing each element with the average of its neighbors.
- Shorten L by (k-1) elements.
- Correctly handle edge cases.
Feedback:
-1 pt Modies L but fails to shorten L by (k-1) elements

"""
def smooth(L, k):
    # User's Answer:
    for i in range(len(L) - (k-1)):
        L[i] = (sum(L[i:3]))/k

#L = [3,4,2,6,1,8]
#print(L)
#smooth(L,3)
#print(L)

"""
Question 2: int2rom(N)
Points: 1 / 4

Specifications:
- Convert an integer N into its Roman numeral representation.
- Handle numbers in descending order and ensure the result is a string.
- Use recursion or iteration effectively.
Feedback:
-3 pts Poorly structured recursion/iteration
n is a int, cant slice an int, Your 2 if checks are also wrong
"""
def int2rom(N, map=(('M', 1000), ('CM', 900), ('D', 500), ('C', 100), ('XC', 90), ('L', 50), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))):

    # User's Answer:
    value = {'M':1000, 'CM':900, 'D':500, 'C':100, 'XC':90, 'L':50, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    if len(N) == 0:
        return ''
    if len(N)>1 and N[:2] in value:
        return [value[:2]] + int2rom(N[2:])
    else:
        return [value[0]] + int2rom(N[1:])
#print(int2rom(1900))

"""
Question 3: countSubstrings(S, start, end)
Points: 0 / 6

Specifications:
- Count the number of substrings within the given range (start, end).
- Correctly handle cases where start == end.
Feedback:
-4pts No answer or fails to meet specication:
    I do not understand how your code matches the specication. It is vastly dierent from the
    intended solution
-2pts Incorrect runtime
"""
def countSubstrings(S, start, end):
    # User's Answer:
    count = 0
    temp = []
    for i in S:
        if i == start:
            temp.append(start)
            count += len(temp)
            temp.pop(start)
        elif i == end:
            temp.append(end)
            count += len(temp)
            temp.pop(end)
        return count
#print(countSubstrings('abcdcbaafb','a','b'))



"""
Question 4: countMatches(S, target)
Points: 1 / 5

Specifications:
- Count how many times the target appears in string S.
- Correctly handle recursion and ensure all matches are accounted for.
Feedback:
-1 pt syntax error
-1 pt Fails to account for within-string matches
-2 pts Fails to handle all required data types
"""
def countMatches(S, target):
    # User's Answer:
    if len(S) == 0:
        return 0
    if target in S[0]:
        return(S.count(target) + countMatches(S[1:],target))
    else:
        return countMatches(S[1:],target)
#print(countMatches({1,(2,1),range(4), 'cs1210',1,((1,))},1))
"""
Question 5: Multisets
Points 2 / 11
"""
#given
class mset:
    def __init__(self,S=()):
        self.D = dict(zip(set(S),[0]*len(set(S))))
        for e in S:
            self.D[e] += 1
    def copy(self):
        new = mset(())
        new.D = self.D.copy()
        return(new)

    """
    Question 5.1: __len__(self)
    0 / 1
    """
    def __len__(self):
    # User's Answer:
        return (len(self))  # Replace with your answer
    # Correct Answer:
        return(sum(self.D.values()))
    
    """
    Question 5.2: __repr__(self)
    0 / 2
    """
    def __repr__(self):
        # User's Answer:
        return(set())  # Replace with your answer

    """
    Question 5.3: __contains__(self)
    0 / 2
    """
    def __contains__(self, element):
        # User's Answer:
        return(element in self)  # Replace with your answer
    #given
    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.difference(other)

    def __xor__(self, other):
        return self.symmetric_difference(other)

    def intersection(self, other):
        result = mset(())
        for k in self.D:
            if k in other.D:
                result.D[k] = min(self.D[k], other.D[k])
        return result
    def difference(self,other):
        result = self.copy()
        for k in other.D:
            if k in result.D:
                result.D[k] -= min(result.D[k], other.D[k])
        return(result)
    """
    Question 5.4: union(self, other)
    Points 1 / 3
    Feedback:
    -1 pt Faliure to sum properly
    -1 pt Fails to produce correct union(beware zero elements)
    """
    def union(self, other):
        # User's Answer:
        result = mset()
        for k in self.D:
            if k in other.D:
                result.D[k] += self.D[k] + other.D[k]
        return result

    """
    Question 5.5: symmetric_difference(self, other)
    Points 1 / 3
    Feedback:
    -2 pts Fails to produce correct symmetric difference (beware zero elements and min/max constraints)
    """
    def symmetric_difference(self, other):
        # User's Answer:
        result = self.copy()
        for k in other.D:
            if k in result.D:
                result.D[k] += max(result.D[k],other.D[k])
        return result
#x = mset((1,1,1,2,3,3))
#y = mset((2,2,2,3,3,4,4,5))
#print(len(x),len(y))