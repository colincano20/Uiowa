'''
1. Simple Functions

'''

'''
PROBLEM #1: 3 lines max
'''
#selection sort, runtime analysis, know when to use recursion or iteration
def notNeighbors(word1,word2):
    #given
    if len(word1) != len(word2):
        return True
    count = 0
# i added this below
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count = count + 1
#given
    return (count != 1)

print(notNeighbors("hay","gay"))
print(notNeighbors("hello","bella"))





'''
PROBLEM #2: fill in lines
'''
def FofF(w, D):
    S = set()  # result set
    for w2 in D[w]: #loop through every word in  the word given
        for w3 in D[w2]: #loop through every dictionary of the close words
            if w3 != w and w3 not in D[w]:    # check if the word is the word, and make sure its not in original dictionary
                S.add(w3) #add word to set 
    return list(S)  #returns list
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
PROBLEM #3: 5 lines max
'''

def nvowels(word):
    count = 0
    for i in word:
        if i in 'aeiou':
            count += 1
    return count

def nvowelsC(word):
    return(len([i for i in word if i.lower() in "aeiou"]))
print(nvowels('BasEball'))
print(nvowelsC('BasEball'))





'''
PROBLEM #4: 5 lines max
'''

from string import punctuation

def avgLen(S):
    w = [len(w.strip(punctuation)) for w in S.split()]
    return (sum(w)/ len(w))


print(avgLen('This is a test of the emergency broadcast system.'))


'''
PROBLEM #5: 8 lines max
'''

def summarize(S):
    result = []
    for i in S.split():
        mid = len(i) // 2
        if len(i) % 2 == 0:
            result.append(i[mid -1: mid+1])
        else:
            result.append(i[mid])
    return ' '.join(result)

def summarize3(S):
    result=[]
    for i in S.split():
        if len(i) % 2 == 0:
            result.append(i[(len(i)//2) -1: (len(i)//2)+1])
        else:
            result.append(i[len(i)//2])
    return ' '.join(result)


def summarize2(S):
    return(' '.join([w[(len(w)-1)//2:len(w)-((len(w)-1)//2)] for w in S.split()]))



print(summarize3( "The rain in Spain stays mainly in the plains" ))

print(summarize2( "The rain in Spain stays mainly in the plains" ))
print(summarize('This is a test of the emergency broadcast system'))


'''
PROBLEM #6: 7 lines max
'''

def flip(L):
    for i in range(len(L) // 2):  # Loop from 0 to half the length of the list L (integer division by 2).
        L[i],L[-(i+1)] = L[-(i+1)],L[i] # Swap the elements at positions i and -(i+1) (i.e., the mirrored index). 0 and -1  1 and -2    2 and -3(same thing) 
    return L #not neededd

print(flip([1,2,3,4,5]))

def flip2(L):
    L[:] = L[::-1]

'''
PROBLEM #7: 8 including helper
'''

def isalpha(S):
    def helper(w):
        w = w.lower()
        return list(w) == sorted(w)
    
    words = S.split()
    return [helper(w) for w in words]

print(isalpha("The rain in spain stays mainly in the plains"))
print(isalpha('His was an ance hers was a king'))

def isalphaA(S):
    def helper(w):
        return(''.join(sorted(list(w))) == w)
    return ( [helper(w.lower()) for w in S.split()])

'''
PROBLEM #8: Matrices
123
456
789
'''
def swapRows(M,i,j):
    M[i],M[j] = M[j],M[i]
    return M

print(swapRows([[1,2,3],[4,5,6],[7,8,9]],0,2))


def swapCols(M, i, j):  # Define the function swapCols, which takes a matrix M and two column indices i and j.
    for w in M:         # Iterate over each row (w) in the matrix M.
        # Swap the elements in the i-th and j-th columns within the current row.
        w[i], w[j] = w[j], w[i]  # 00 'i1' swap with 00 '3'
    return M            # Return the modified matrix M.

def swapCols2(M,i,j):
    for x in range(len(M)):
        M[x][i], M[x][j] = M[x][j], M[x][i]
    return M

print(swapCols([[1,2,3],[4,5,6],[7,8,9]],0,2))    #M[0][1]
print(swapCols2([[1,2,3],[4,5,6],[7,8,9]],0,2))    #M[0][1]


def mirror(M):
    for i in range(len(M)):   # i=0,  i=1    i=2 not needed as j starts from i+1
        for j in range(i+1,len(M)):         #when i = 0  j=1 then j=2   when i=1 j=2
            M[i][j],M[j][i] = M[j][i], M[i][j]     # This line swaps the elements at position [i][j] with the elements at position [j][i] in the matrix M
    return M

print(mirror([[1,2,3],[4,5,6],[7,8,9]]))




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


'''
2. Algorithms and Efficiency
'''
'''
Problem 1
'''

import random 
def MofN(N,M):
    L=[]                                  #1 O(1)
    j = M                                 #2 O(1)
    for i in range(N):                    #3 O(N)
        if random() <= j / (N-i):         #4   O(1)
            L.append(i)                   #5   O(1)
            j = j-1                       #6   O(1)
    return(L)                             #7 O(1)

'''
it is O(N) because first two assignment statements are O(1)(1,2)
the for loop executes N time(3)
the body of the if consists of rwo O(1) assignments(5,6)
'''









'''
3. Recursion
'''




def deepFlip(L):
    if type(L) is not list:
        return L
    flip(L)
    for item in L:
        deepFlip(item)
    return L
print(deepFlip([1,2,[3,4,5],6,[7],9]))








'''
Specification: Write a function wordLengthHistogram(S) that takes a string S containing a sentence and returns
 a dictionary where the keys are word lengths and the values are the 
number of words of that length in the sentence. Ignore punctuation and consider only alphabetic characters.
'''

def wordLhistogram(S):
    D = {}
    for w in S.split():
        if len(w) in D:
            D[len(w)] += 1
        else:
            D[len(w)] = 1
    return D




print(wordLhistogram("Hello my name is Colin Cano and I love baseball"))



'''
Specification: Write a function columnSum(matrix)
 that takes a 2D list matrix representing a matrix and returns a list of sums of each column.

 123
 456
 789
'''

def columnSum(L):
    if not L:
        return []
    sums = [0] * (len(L[0]))
    for i in L:
        for j in range(len(L[0])):
            sums[j] += i[j] 
       
    return sums
        

print(columnSum([[1,2,3],[4,5,6],[7,8,9]]))




def sumOfDigits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10  # Add the last digit to sum_digits
        n = n // 10  # Remove the last digit
    return sum_digits

# Test cases
print(sumOfDigits(123))  # Example output: 6 (1 + 2 + 3)


def sss(L):
    squares = [x**2 for x in L if x % 2 == 0]
    return squares


print(sss([1, 2, 3, 4, 5, 6]))



def sumOfEvenNumbera(L, result = 0):
    if not L:
        return result
    if L[0] % 2 == 0:
        result += L[0]
    return (sumOfEvenNumbera(L[1:],result))
    
    
def sumOfEvenNumbers(L):
    return sum(x for x in L if x % 2 == 0)

def multiplicationTable(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
print(multiplicationTable(4))

print(sumOfEvenNumbera([2,2,3,4,5,6]))


def flattenlist(L):
    result= []
    for i in L:
        if isinstance(i,list):
            result.extend(flattenlist(i))
        else:
            result.append(i)
    return result

print(flattenlist([1,[2,3],4,5]))


def filter(S,i):
    result = []
    for w in S:
        if len(w) >= i:
            result.append(w.capitalize())
    return result

print(filter(['list', 'Python', 'No', 'Witchcraft'], 3))


def countC(S):
    count = 0
    D = {}
    for i in S:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1

    return D
        




print(countC('Hello colin what is up')) 
print(summarize3( "The rain in Spain stays mainly in the plains" ))
print(swapCols2([[1,2,3],[4,5,6],[7,8,9]],0,2))    #M[0][1]