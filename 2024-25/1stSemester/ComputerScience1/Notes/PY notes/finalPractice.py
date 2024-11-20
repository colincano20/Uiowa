'''
1. ComboSum
Consider the function comboSum(N, B, R=()) which takes an integer, N, and a "basket" of unique (i.e., no
duplicates) integers, B, and returns a list of tuples, where each tuple represents a collection of integers
from B that sum to to N. So, for example:
>>> comboSum( 10, [ 5, 3, 2 ] )
[ ( 2, 2, 2, 2, 2 ), ( 3, 3, 2, 2 ), ( 5, 3, 2 ), ( 5, 5 ) ]
>>> comboSum( 12, [ 3, 4 ] )
[ ( 4, 4, 4 ), ( 3, 3, 3, 3 ) ]
>>> comboSum( 17, ( 2, 6, 4 ) )
[ ]
A partial implementation of comboSum() that uses the extra argument R to "collect" partial results is
shown below: fill in the remaining blanks.

'''

def comboSum(N,B,R=()):
    if N==0: #base case
        return [R]
    elif N < 0 or not B: #base case
        return([])
    return(comboSum(N, B[1:],R)+ comboSum(N-B[0],B,R+(B[0],))) #recursive call

#arguement: In each recursive call, B is reduced by one element when the function excludes the first element (B[1:]).
#Once B is empty (not B), the base case is triggered, ensuring no infinite recursion. When the first element of B is included (N - B[0]), the value of N decreases.
#If N becomes less than 0, the base case (N < 0) ensures termination.
print(comboSum(10, [5, 3, 2]))



'''
2. Fill in the Blank
Dictionaries, Lists, and Sets are mutable,
Strings and Tuples are immutable.
'''
'''
3. Pancake Flipping
Before he dropped out of Harvard, started Microsoft, and become the world’s richest man, Bill Gates
partnered with then-Berkeley now-Columbia Professor Christos Papadmitriou to publish a paper entitled
Bounds for Sorting by Prefix Reversal. The paper addresses a question originally posed by Harvard
Professor Harry Lewis: given a stack of N different size pancakes and a spatula, how many "flips" of
pancakes at the top of the stack are required to sort them from largest (bottom) to smallest (top)? Gates
showed that this problem, known as the pancake sorting problem, can theoretically be solved in 1.67
spatula operations per pancake, or 1.67*N flips.
Here, we model the pancake stack as list of unique integers. Pancake sorting differs from the other
algorithms we have studied in that the only operation we can apply is to invert the order of the first part of
the list (the "top of the stack," so to speak); we cannot for example exchange individual elements of the
stack. So the types of swapping transformations we applied in insertion sort (e.g., [1, 2, 3, 4, 5] => [1, 5,
3, 4, 2]) are not legal here: only operations like [1, 2, 3 | 4, 5] => [3, 2, 1 | 4, 5] or [1, 2, 3, 4 | 5] => [4, 3,
2, 1 | 5] are legal.
Thus the only basic operation in pancake sorting is to modify L by "flipping" the top k "head" elements of
L. Complete the function to do so:
de f fli pHe a d (L, k ) :
[3, 2, 1 | 4, 5]
'''

def flipHead(L,k):
     return L[:k][::-1] + L[k:]


stack = [3, 2, 1, 4, 5]
k = 3
#print(flipHead(stack, k))  # Output: [1, 2, 3,| 4, 5]


'''
Armed with your completed flipHead(L, k) implementation, we’re ready to sort pancakes. The easiest
algorithm applies the following flip operations to successively "shorter" tops of the stack:
find the maximum value in L;
flip enough of L to bring the max value to front; then
flip all of L, placing max value at end.
Using the pancake stack analogy: find the largest element (largest pancake) in the list (stack), and flip just
enough pancakes to bring that element to the front. Then flip the entire stack of pancakes to bring the
largest pancake from front to bottom. Once the largest pancake is in its desired position, repeat the
process on the top N-1 pancakes only, thus shortening the stack by 1 pancake each time. So using | to
indicate spatula placement:
round find max → after flip1 → after flip2
1 [ 3, 2, 4, 5 | 1 ] → [ 5, 4, 2, 3, 1 |] → [ 1, 3, 2, 4, 5 ] → next round
2 [ 1, 3, 2, 4 | 5 ] → [ 4, 2, 3, 1 | 5 ] → [ 1, 3, 2, 4, 5 ] → next round
3 [ 1, 3 | 2, 4, 5 ] → [ 3, 1, 2 | 4, 5 ] → [ 2, 1, 3, 4, 5 ] → next round
4 [ 2 | 1, 3, 4, 5 ] → [ 2, 1 | 3, 4, 5 ] → [ 1, 2, 3, 4, 5 ] → [ 1, 2, 3, 4, 5 ]
Note that for a stack of N pancakes, you will perform these operations N-1 times, resulting in 2(N-1) flips,
just a few more flips than Gates’ and Papadimitriou’s theoretically optimal 1.67*N flips.
2 Revised December 5, 2024

'''


def pancakeSort(L):
    #print(L)
    if len(L) <= 1:  # Base case
        return L
    
    k = L.index(max(L)) + 1

    L = L[:k][::-1] + L[k:]
    L = L[::-1]
    
    return pancakeSort(L[:-1]) + [L[-1]] 

# Example usage
print(pancakeSort([3, 2, 4, 5, 1]))
# Output: [1, 2, 3, 4, 5]

'''
4. Uniquify
Write a function, uniquify(L), that takes a list of elements and returns a new list that removes duplicates
but returns the elements in exactly the same order in which they first appear. So, for example:
>>> uniqui f y( [ 1, 2, 3, 2, 4, 2, 3, 5 ] )
[1 , 2, 3, 4, 5 ]
>>> uniqui f y( l is t ( 'substitute'))
[ 's','u','b','t','i','e'] .
>>> uniqui f y( l is t ( ' ba zook a '))
[ ' b' , ' a ', ' z' , ' o ', ' k' ]
def uniquify (L) :
'''
def uniquify(L):
    new = []
    for i in L: #O(N)
        if i not in new: #O(N)
            new.append(i)
    return new
    #The algorithmic runtime of the provided uniquify function is O(N²). O(N * N)

    '''
    new = []
    for i in L:
        print(L)
        if i not in new:
            new.append(L[i])
            print(new)
    return new
   
    '''
   
   #return list((set(L)))
#print(uniquify( [ 1, 2, 3, 2, 4, 2, 3, 5,69] ))
#print(uniquify(list('substitute')))

'''
5. Increasing Circular Sequences
Let a circular sequence be a list of unique values such that the first element follows the last element, and
the last element precedes the first element. Thus the lists [1, 4, 5, 2], [4, 5, 2, 1], [5, 2, 1, 4] and [2, 1, 4, 5]
are all just different representations of the same circular sequence.
An increasing circular sequence is a circular sequence with the added property that, with one exception,
the numbers all appear in increasing order. Thus [4, 5, 1, 2] is an increasing circular sequence, while [5, 4,
1, 2] is not (to see why this is so, consider that [4, 5, 1, 2] is the same circular sequence as [1, 2, 4, 5],
while [5, 4, 1, 2] is instead written [1, 2, 5, 4]). Note also that  is an increasing circular sequence,
as is [’e’, ’f’, ’k’, ’w’, ’z’, ’a’]: these needn’t always be just "lists of numbers."
We could find the minimum value in a circular sequence using the Python min() function (it is, after all,
often just a list) or instead by exploiting the special structure of the circular sequence. Write an efficient
function that returns the minimum value in a circular sequence by exploiting the fact that the minimum
value is the only item in the sequence that follows a value larger than itself. Hint: remember, you can
assume that each value in the sequence is unique, and that the input C will always an increasing circular
sequence.
de f mi nCi r cu l ar (C) :
'''
def minCircular(C):
    if type(C) != list:
        return(minCircular(list(C)))
    if len(C) == 1:
        return C[0]
    elif C[1] > C[0]:
        C.pop(1)
        return(minCircular(C))
    else:
        C.pop(0)
        return(minCircular(C))

print(minCircular([1, 4, 5, 2]))
print(minCircular(['e','f','q','c','a','b']))
print(minCircular('zaefkw'))



'''
We can extend the notion of a circular sequence to allow for a subsequence of decreasing values in
addition to the subsequence of increasing values. Such a sequence would still have two extrema, a
minimum value and a maximum value (remember, the values are still unique), but they might be separated
by several uniformly increasing or uniformly decreasing intermediate values.
So, for example, our [4, 5, 1, 2] circular sequence remains legal, but now [4, 5, 3, 1, 2] is also a legal
circular sequence. The minimum value (1) and the maximum value (5) remain unchanged, but the
transition from max to min need not be so abrupt; the [5, 3, 1] decreasing subsequence would not have
been allowed under our previous definition. Some more examples:
(1) The sequence [2, -2, 1, 4, 6, 7] is legal, because it is equivalent to the sequence [-2, 1, 4, 6, 7, 2]
which increases as [-2, 1, 4, 6, 7], then decreases as [7, 2, -2].
(2) Similarly, the sequence [9, 2, -4, -10, -5] is legal, as it is equivalent to [-10, -5, 9, 2, -4] which
increases as [-10, -5, 9] and decreases as [9, 2, -4, -10].
(3) The sequence [1, 3, 12, 4, 2, 10] is not legal, because there is no circular shift that can change the
fact that the sequence has two distinct local maxima (at 12 and 10), separated by a mimiuma at 2.
The subsequences here would be [1, 3, 12], [12, 4, 2], [2, 10] and [10, 1].
(4) The sequence [2, 3, 4, 1] is (still) legal, as the equivalent sequence [1, 2, 3, 4] increases as [1, 2, 3,
4] and then decreases (abruptly) as [4, 1].
Write an efficient function, checkSequence(L), that takes a list, L, and returns True if it is a legal sequence
and False otherwise. The ideal solution will once again take advantage of the special structure of the
sequence and should not resort to explicity shifting the sequence around, nor will it need to separately
consider zero-length increasing or decreasing subsequences.
de f che ckSe qu e n c e (L) :
'''

def checkSequence(L):
    pass


'''
Specification:
Write a function findDivisibleSubsets(nums, k) that takes a list of integers nums and a positive integer k. 
The function should return all subsets of nums where the sum of elements in each subset is divisible by k.
findDivisibleSubsets([1, 2, 3, 4, 5], 3)  
# Output: [[3], [1, 2], [3, 6], [4, 5], ...]
'''

def findDivisibleSubsets(L,k):
    result = []
    if len(L) == 0:
        return result
    elif not k:
        pass