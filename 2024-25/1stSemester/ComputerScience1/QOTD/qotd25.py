# CS1210: QotD25
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["cmcano"])

######################################################################
# Specification: Consider a dictionary, D, that associates, e.g.,
# student IDs with (integer) scores on an assignment. Write a
# function, flipDictionary(D), that returns the inversion of D (a new
# dictionary), such that the values in D are keys in the new
# dictionary and the keys of D are the values in the new dictionary.
#
# Example:
#   >>> D
#   {'John':55, 'Terry':62, 'Eileen':76, 'Cyrus':76, 'Joanne':65}
#   >>> flipDictionary(D)
#   {55: ['John'], 62: ['Terry'], 76: ['Eileen', 'Cyrus'], 65: ['Joanne']}
#
def flipDictionary(D):
    newD = {}
    for i, j in D.items():
        if j not in newD:
            newD[j] = []
        newD[j].append(i)
    
    return newD
D = {'John':55, 'Terry':62, 'Eileen':76, 'Cyrus':76, 'Joanne':65}
print(flipDictionary(D))
