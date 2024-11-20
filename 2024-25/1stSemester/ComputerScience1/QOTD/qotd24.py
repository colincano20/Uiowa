# CS1210: QotD24
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
# Specification: mostFrequentElements(S) takes a sequence, S, and
# returns a tuple containing the most commonly occuring element(s) in
# S. The tuple will have only one element, unless there is a tie.
#
def mostFrequentElement(S):
    D = {}
    for i in S:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
           
            
    result = [x for x, value in D.items() if value == max(D.values())]
    return tuple(result)



print(mostFrequentElement(['a', 'b', 'b', 'a', 'c']))
# Expected Output: ('a', 'b')
print(mostFrequentElement(['a']))
# Expected Output: ('a',)
print(mostFrequentElement(['a','b','c']))
# Expected Output: ('a','b','c')

