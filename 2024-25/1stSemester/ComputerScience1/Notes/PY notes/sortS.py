#SPECIFATION
# the function, sortS(L), takes a list of strings, and sorts them alphyabetically
#1. Reverse a String
#Specifications:

#Function name: reverse_string(S)
#Input: A string S.
#Output: Return the string S reversed.



def reverseS(S):
    return(list(S).reverse())

#adds up List of integers
def sumL(L):
        if len(L) > 1:
            return( sum(L[0:]))
        else:
            return L
    

    


#max_num([1, 2, 3, 4])  # Output: 4
#max_num([-5, 0, 20, 3])  # Output: 20

def maxNum(L):
    return(max(L))

#checks if integer is even.
def isEven(i):
    return( (i % 2) == 0 )



#Output: Return the number of vowels (a, e, i, o, u) in the string.

def cntV(S):
    return( S.lower() in 'aeiou')



