'''Complete each of the following functions, presented roughly in order of difficulty. Each problem should
fundamentals of public health

take no more than a couple of lines of code, and should not exceed the number of lines provided (but
may well require fewer). Maximum points will be awarded for elegance and good style; comment as
appropriate (comments don’t count as lines used; best to place them to the side).
(1) Recall the WordNet code we developed in class. Complete the following function that compares
two words and returns True if the two words cannot be considered neighbors. Recall that two
words are neighbors if they differ in one and only one character position.

3 lines

'''
def notNeighbors(word1,word2):
    if len(word1) != len(word2):
        return True
    count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count = count + 1

    return (count != 1)

print(notNeighbors("hay","gay"))
print(notNeighbors("hello","bella"))






'''Recall the WordNet dictionary we constructed in class, where each key was a 5 letter word and
each value was a list of other 5 letter words that differed by exactly one letter from the key.
Complete the following function, which takes a word, w, and the word net dictionary, D, as inputs
and returns a list of words reachable from w in exactly two hops ("friends of friends," so to speak)
but not less.
def FofF(w, D):
S=set() # result set
for w2 in D[w]:
for ______________________________________
'''

def FosF(w,D):
    
    S = set() #result set
    for w2 in D[w]:
        for w3 in D[w2]:
            if w3 != w and w3 not in D[w]:
                S.add(w3)
    return list(S)
       
def FofF(w, D):
    S = set()  # result set
    for w2 in D[w]:
        for w3 in D[w2]:
            if w3 != w and w3 not in D[w]:
                S.add(w3)
    return list(S)

D = {
    'apple': ['apply', 'ample', 'appel'],
    'apply': ['apple', 'aptly', 'amply'],
    'ample': ['apple', 'amply', 'ample'],
    'appel': ['apple', 'ampel', 'appli'],
    'aptly': ['apply', 'aptly', 'artly'],
    'amply': ['apply', 'ample', 'ample'],
    'ampel': ['appel', 'ampel', 'ample'],
    'appli': ['appel', 'appli', 'apply'],
    'artly': ['aptly', 'artly', 'apely'],
    'apely': ['artly', 'apely', 'apply']
}

print(FofF('apple', D))





'''
In the English language, the letters ’aeiou’ are considered vowels and the remaining letters are
considered consonants. Complete the following function that returns the number of vowels in a
word.
de f nv owe l s (wo r d ) :
max 5 lines
'''


def nvowels(word): #might be too many lines
        vowels = 'aeiou'
        count = 0
        for i in word:
            if i in vowels: 
                count = count + 1
        return count
def nvowels1(word):
    vowels = 'aeiou'
    return sum(1 for i in word if i in vowels) #uses a generator expression with sum(), which counts 1 for each vowel found in word.

print(nvowels('banana'))
print(nvowels1('banana'))




'''
Write a function that takes a string, S, as its input and returns a floating point number indicating
the average length of the words in S. So:
>>> f r om s tri ng imp o rt pun c t u at i on
>>> pun c t u at i on
’ ! " #$%&´ ( ) *+ , -. / : ; <=> ?@[ \ \ ] ˆ_‘ { | } ˜ ’
>>> avgLe n ( ’Th i s i sa t es t of t he eme r gency b r o adc a st s ys t em ’ )
4.444444444444445
While you can presume there’s at least one space between every word, you should strip any
punctuation marks from both ends of the individual words before computing the average length
(you can go ahead and use the punctuation variable, which has already been imported from the
string module).
def avgLen(S):

'''
from string import punctuation

def avgLen(S):
    words = S.split()
    word = [word.strip for word in words]
    return sum(len(word) for word in words) / len(words)


print(avgLen('.Hello! How are you Today'))
print(avgLen('This is a test of the emergency broadcast system.'))


            

#word = S.split()
#   clean = []
#    for i in word:
#        clean.append(word.strip(punctuation))
#   return word        # (len(S.split())) #word total
''''''

''' Write a function summarize() that takes a sentence and returns a new sentence, formed by
reducing each word to only one or two characters taken from the middle of the word, depending
on whether the word is of even or odd length.

>>> summarize( "The rain in Spain stays mainly in the plains" )
’ h ai in a a in in h ai ’
>>> s umma r i z e( "Th i s i sa t es t of t he eme r gency b r o adc a st s ys t em " )
’ h i i s a es of hgd s t ’

8 lines max
'''



def summarize(S):
    w = S.split()
    result = []
    for word in w:
        mid = len(word) // 2
        if len(word) % 2 == 0:
            result.append(word[mid - 1: mid+1])  # Adjusting the index for even-length words
        else:
            result.append(word[mid])
    return ' '.join(result)


print(summarize( "The rain in Spain stays mainly in the plains" ))








'''
Implement a function flip(L) that flips the internal representation of a list L, without using
L.reverse() to do so. Your function should modify L rather than return a new list.
de f fli p (L) :
_____
max 7_
>>> L = [0 , 1, 2, [3 , 4] , 5 ]
>>> fli p (L)
>>> L
[5 , [3 , 4] , 2, 1, 0 ]


Note that the function doesn’t return anything, but rather modifies L.
'''

def flip(L):
    for i in range(len(L) // 2):
        L[i], L[-(i+1)] = L[-(i+1)], L[i]
    print(L)
print(flip([0,1,2,[3,4],5]))










'''
Consider interpreting a list of lists as a representation for a matrix. For example, the matrix:

123             321
456             654
789             987

789              987
456              654
123              321

would be represented as:
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
where each element of the list corresponds to a row of the matrix. You may assume that the
matrix is well formed, that is, that every row is of the same length, but you cannot assume that the
number of rows and columns is the same. Write two functions that manipulate (that is, mutate)
the matrix in the following ways. The first function exchanges (i.e., swaps) two specified rows,
while the second exchanges two specified columns:
>>> m = [ [1 , 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
>>> swa pRows (m, 0 , 2 )
>>> m
[ [ 7, 8, 9 ], [ 4, 5, 6 ], [ 1, 2, 3 ] ]
>>> swa pCo l s (m, 0 , 2 )
>>> m
[ [ 9, 8, 7 ], [ 6, 5, 4 ], [ 3, 2, 1 ] ]


'''

def swapRows(M, i, j):
    M[i], M[j] = M[j], M[i] # Swap the rows at indices i and j in the matrix.
    return M
    


def swapCols(M, i, j):  # Define the function swapCols, which takes a matrix M and two column indices i and j.
    for w in M:         # Iterate over each row (w) in the matrix M.
        # Swap the elements in the i-th and j-th columns within the current row.
        w[i], w[j] = w[j], w[i]  
    return M            # Return the modified matrix M.

                


def mirror(M):
    for i in range(len(M)):   # i=0,  i=1    i=2 not needed as j starts from i+1
        for j in range(i+1,len(M)):         #when i = 0  j=1 then j=2   when i=1 j=2
            M[i][j],M[j][i] = M[j][i], M[i][j]     # This line swaps the elements at position [i][j] with the elements at position [j][i] in the matrix M
    return M


'''
Write a function that multiplies two matrices, M and N, provided the input matrices compatible in
size. Should return a new matrix, or None if the matrices are not size compatible
10 max 

123                    7  8
456                    9  10
                       11 12
'''
def multiply(M,N):
    if len(M[0]) != len(N):
        return None
    result = [[0 for x in range(len(N[0]))] for y in range(len(M))]  #Initialize the result matrix with zeros. The size is (rows of M) x (columns of N)
    for i in range(len(M)):  # Loop through each row index of matrix M.
        for j in range(len(N[0])):  # Loop through each column index of matrix N.
            for k in range(len(N)):  # Loop through each element index of the row of M and the column of N.
                result[i][j] += M[i][k] * N[k][j]  # Calculate the dot product and add it to the corresponding position in the result matrix.

    return result

    






print(multiply([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))
# [58,64][139,154]   1*7 +2*9 + 3*11             1*8 + 2*10 + 3*12   4*7 + 5*9 + 6*11

print(mirror([[1,2,3],[4,5,6],[7,8,9]]))
    
print(swapCols([[1,2,3],[4,5,6],[7,8,9]],0,2))    #M[0][1]
    
    
print(swapRows([[1,2,3],[4,5,6],[7,8,9]],0,2))




















'''

2. Algorithms and Efficiency
Givenacollection of N things, you want to select a subset of size M ≤ N from the original collection at
random, while ensuring that every element in the original collection has an equal probability of being
selected. To make the problem a little simpler, let’s assume that the N things are simply the values in
list(range(N)), and you would like the selected numbers to be returned in order.
Your general strategy is as follows: consider each of the N numbers in order. When considering the ith
element, select it for inclusion with probability j
N−i
, where 0 < j ≤ M is the number of elements left to be
selected. When you select an element, decrement j, otherwise leave it alone.
This should remind you of the shuffle function provided in the current homework. If M = 1, then you
simply consider selecting each successive element in range(N) with probability 1
N−i
. When you finally
select an element, the probability another element gets selected drops to 0
N−i
. On the other hand, if
M = N, then every element is considered for selection with probability M
N−i which remains 1 as i gets
larger and j gets smaller in lockstep.
(1) Complete the following outline for the function in question (recall random() returns a random
float between 0 and 1).
def MofN(N, M):
L=[] # 1
j=M # 2
for i in range(N): # 3
if random() <= ___________________: # 4
___________________________ # 5
j=j-1 # 6
return(___________________) # 7
(2) Using "order of" notation, what is the runtime of this algorithm in terms of N? Explain how you
computed the expected runtime; feel free to use the numbers out to the right of the function to
refer to individual lines.


'''
import random 
def MofN(N,M):
    L=[]                                  #1
    j = M                                 #2
    for i in range(N):                    #3
        if random() <= j / (N-i):         #4
            L.append(i)                   #5
            j = j-1                       #6
    return(L)                             #7



'''

The main loop runs N times (for each i in range(N)), which is line 3.

Inside the loop, there's a constant time check of the random number against the computed probability. This check takes O(1) time (line 4).

If an element is selected, adding it to the list takes O(1) time (line 5).


Since the loop runs 
N times, and within each iteration, we are performing O(1) operations, the expected runtime of this algorithm is:
O(N)

'''


'''
3. Recursion [6 points]
In question 1.6 above, you implemented a function flip() that modifies a list, reversing its elements.
Extend this function so as to flip the input list even when the list is ‘‘deep.’’ In other words, while the
current implementation behaves like this:
>>> L = [0 , 1, 2, [3 , 4] , 5 ]
>>> fli p (L)
>>> L
[5 , [3 , 4] , 2, 1, 0 ]
the new implementation should behave like this:
>>> L = [0 , 1, 2, [3 , 4] , 5 ]
>>> d e e pF l i p (L)
[5 , [4 , 3] , 2, 1, 0 ]
>>> L
[5 , [4 , 3] , 2, 1, 0 ]
Notice the ‘‘deep’’ flip that happens inside what was originally L[3]; also notice that deepFlip(L), unlike
flip(L), returns the flipped list.
12 max
'''

        
def deepFlip(L):
    if len(L) <= 1:
        return L
    result = deepFlip(L[1:-1])
    return (L[-1] + result + L[0])



print(deepFlip([0 , 1, 2, [3 , 4] , 5 ]))























