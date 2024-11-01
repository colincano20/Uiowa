#Write a function countChar(S, char) that takes a string S and a character
#char as input, and returns the number of occurrences of char in S.
#>>> countChar('hello world', 'l')
#3
#>>> countChar('university', 'i')
#2
#>>> countChar('CS1210', '1')
#1
def countChar(S,char):
    count = 0
    if len(S) == 0 :
        return 0
    for i in S:
        if char == i:
            count = count + 1
    return(count)
        
print(countChar('hello world', 'l'))


#Write a function filterEvens(L) that takes a list
#L of integers and returns a new list containing only the even numbers from L.
#>>> filterEvens([1, 2, 3, 4, 5, 6])
#[2, 4, 6]
#>>> filterEvens([7, 11, 13])
#[]
#>>> filterEvens([8, 0, 12])
#[8, 0, 12]

def filterEvens(L):
    return([c for c in L if c%2 == 0])

print(filterEvens([1, 2, 3, 4, 5, 6]))

#Write a function reverseWords(S) that takes a string S as input and returns
#a new string where the words in S are reversed, but their order is preserved.
#>>> reverseWords('Seize the day')
#'ezieS eht yad'
#>>> reverseWords('hello world')
#'olleh dlrow'
#>>> reverseWords('Python programming')
#'nohtyP gnimmargorp'

def reverseWords(S):
    return( ' '.join([c[::-1] for c in S.split()]))

print(reverseWords('hello world'))




#Write a function findFirstVowelCluster(S) that takes a string S and returns the
#first vowel cluster (sequence of contiguous vowels) in S. If no vowel cluster
#exists, return an empty string.
#>>> findFirstVowelCluster('This is a test')
#'i'
#>>> findFirstVowelCluster('Master Winnie the Pooh')
#'a'
#>>> findFirstVowelCluster('rhythm')
#''

def findFirstVowelCluster(S): 
    vowels = 'aeiouAEIOU'  # Case-insensitive vowel checking
    cluster = ''  # This will store the vowel cluster when found
    for c in S:
        if c in vowels:
            cluster += c  # Add vowels to the cluster
        elif cluster:  # If we've already started a cluster, break on first non-vowel
            return cluster  # Return the cluster when it ends
    return cluster  # If we find a cluster at the end, return it; otherwise, it's empty



print(findFirstVowelCluster('This is a test'))




























