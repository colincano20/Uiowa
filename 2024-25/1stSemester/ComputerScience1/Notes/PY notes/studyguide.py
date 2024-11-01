'''. Loop Challenge: Write a function that finds the second largest number
in a list using:
a. A for loop
b. A while loop
'''

def largeF2(L):
    if len(L) < 2:
        return None
        
    # First find the largest
    largest = L[0]
    for i in L:
        if i > largest:
            largest = i
            
    # Then find the largest number that's not equal to largest
    second = None
    for i in L:
        if i < largest:  # must be less than largest
            if second is None or i > second:  # either first valid number or bigger than current second
                second = i
                
    return second
print(largeF2([5, 2, 8, 1, 9, 3]))
#While 
def largeW2(L):
    # Handle lists that are too short
    if len(L) < 2:
        return None
        
    # First find the largest
    largest = L[0]
    i = 0
    while i < len(L):
        if L[i] > largest:
            largest = L[i]
        i += 1
            
    # Then find the largest number that's not equal to largest
    second = None
    i = 0
    while i < len(L):
        if L[i] < largest:  # must be less than largest
            if second is None or L[i] > second:  # either first valid number or bigger than current second
                second = L[i]
        i += 1
                
    return second
print(largeW2([5, 2, 8, 1, 9, 3]))







''' List Comprehension Challenge: Write a list comprehension
that generates all pairs of numbers (x,y) where:
x is from 0 to 3
y is from 0 to 3
x + y is even
'''

def listC(x,y):
    return([(x,y) for x in range(4) for y in range(4) if ((x + y) % 2 == 0)])

print(listC(1,2))



'''
Recursion Challenge: Write a recursive function that counts
how many times a specific element appears in a list.
'''

def recC(L,target):
    if L == []: # Base case: if the list is empty, function keeps going till this is true
        return 0
    if L[0] == target: # Check if the first element matches the target
        return (1 + recC(L[1:],target))  # Count this occurrence and recurse
    else:
        return(recC(L[1:], target))  # Just recurse without counting

print(recC([69,69,8,7,6,5,1,69,69,7], 69))
    



'''
find and fix error

def find_max(L):
    max_value = 0
    for x in L:
        if x > max_value:
            max_value = x
    return max_value
'''

def find_max(L):
    if L == []:
        return None
    max_value = L[0] # Start with first element, not 0
    for x in L:
        if x > max_value:
            max_value = x
    return max_value

print(find_max([-1,-5,-4,-69]))
print(find_max([]))



'''
fix while loop
i = 1
while i < 10:
 print(i)
 '''

def w():
    i = 0
    while i < 10:
        print(i)
        i += 1

print(w())


'''
debug recursive function
def sum_list(lst):
    return lst[0] + sum_list(lst[1:])
'''


def sum_list(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([5,4,5,1]))




'''
Practice Implementation Tasks
'''




'''
Implement both iterative and recursive versions of:
Fibonacci sequence
Sum of a list
Reverse a string
'''


def revSr(S):
    if len(S) == 0:
        return None
    else:
        return(S[:-1])

print(revSr("Hello World"))






'''
Create a function that removes duplicates from a list:
Using a set
Using a loop without sets Compare the efficiency of both approaches
'''


def remDupS(L):
    return(set(L))

print(remDupS([4,3,5,5,6,6,6,7,8,9]))
    
def remDupI(L):
    result = []
    for i in L:
        if i not in result:  # Check if the item is already in the result
            result.append(i) # Add it if it's not a duplicate
    return result
                


print(remDupI([4,5,5,5,6,6,6,7,8,9]))




'''
Write a function that checks if a string is a palindrome:
Using a while loop
Using recursion
'''




def palindromeW(S):
    left = 0                 # Initialize left pointer
    right = len(S) - 1      # Initialize right pointer

    while left < right:      # Continue until the pointers meet
        if S[left] != S[right]:  # Check if characters are not equal
            return False          # Not a palindrome
        left += 1                # Move the left pointer to the right
        right -= 1               # Move the right pointer to the left

    return True  # If all characters matched, it's a palindrome


print(palindromeW("racecar"))
print(palindromeW("racecars"))



def palindromeR(S):
    if len(S) <= 2:
        return True
    return(S[0] == S[-1] and palindromeR(S[1:-1]))
#If these characters equal, the function then calls itself recursively with s[1:-1],
#which removes the first and last characters from the string. The recursion continues until it either confirms that the string is a palindrome or reaches the base case.




print(palindromeR("racecar"))
print(palindromeR("racecars"))



