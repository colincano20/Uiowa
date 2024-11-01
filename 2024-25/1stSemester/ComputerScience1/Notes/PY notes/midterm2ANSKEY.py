'''
1. Simple Functions

'''

'''
PROBLEM #1: 3 lines max
'''

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
    vowels = 'aeiou'
    count = 0
    for i in word.lower():
        if i in vowels:
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
    ' '.join(S)
    return(len(S) - len(S.split()))  / len(S.split())


def avgLen1(S):
    return sum(len(word.strip(punctuation)) for word in S.split()) / len(S.split())

def avgLenC(S):
    avg = 0
    for word in S.split():
        avg += len(word.strip(punctuation))
    return(avg/len(S.split()))

def avgLen2(S):
    # Split the string into words
    words = S.split()
    lengths = [len(word.strip(punctuation)) for word in words]
    average_length = sum(lengths) / len(lengths)
    
    return average_length

print(avgLen2('This is a test of the emergency broadcast system.'))
print(avgLen2('Hello! How are you Today?'))
print(avgLen1('This is a test of the emergency broadcast system.'))
print(avgLen1('Hello! How are you Today?'))
print(avgLen('This is a test of the emergency broadcast system.'))
print(avgLen('.Hello! How are you Today'))

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

print(summarize( "The rain in Spain stays mainly in the plains" ))
print(summarize('This is a test of the emergency broadcast system'))


'''
PROBLEM #6: 7 lines max
'''

def flip(L):
    for i in range(len(L) // 2):  # Loop from 0 to half the length of the list L (integer division by 2).
        L[i],L[-(i+1)] = L[-(i+1)],L[i] # Swap the elements at positions i and -(i+1) (i.e., the mirrored index). 0 and -1  1 and -2    2 and -3(same thing) 
    return L

print(flip([1,2,3,4,5]))


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

print(swapCols([[1,2,3],[4,5,6],[7,8,9]],0,2))    #M[0][1]


 
