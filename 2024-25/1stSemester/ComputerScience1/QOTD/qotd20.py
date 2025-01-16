# CS1210: QotD20
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
# Roman numerals are strings of characters that are read from left to
# right. Each character represents a specific value:
#    M=1000, D=500, C=100, L=50, X=10, V=5 and I=1
# If sorted from larger to smaller, a string of these would then
# be interpreted as the sum of those elements. So:
#    MDCLXXXV = 1000+500+100+50+10+10+10+5 = 1685
# In addition, two character combinations arranged from smaller to
# larger are also allowed. Thus we can use IV rather than IIII to
# represent the number 4, and MCM to represent 1900.
#
# Specification: rom2int(R) takes a string, R, representing a legal
# Roman numeral, and returns the equivalent integer.
#
# A Roman numeral is legal if it is generally arranged from largest
# value to smallest, with the exception of allowing a
# single-small-large-letter combination at the end of the string of
# "large" letters. Thus "XXIXV" is legal, but "XIXXV" is not.
#
# Hint: an iterative approach seems warranted, traversing R
# left-to-right while accumulating is integer counterpart.
#
# Hint: please, no giant if/elif/else statements checking each Roman
# numeral character; you know better than that by now!
#
# Here, you can assume that the input R is a legal Roman number; in
# other words, if R is illegal, any answer is correct.
#
# Example:
#   >>> rom2int("MCCX")
#   1210
#   >>> rom2int("MCMXCIV")
#   1994
#
def rom2int(R):
    Dict = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } #dictionary
    total = 0
    previous = 0 
    for i in R: #loop through string
        if Dict[i] > previous:
            total += Dict[i] - 2 *previous   #subtracts if index is bigger then previous
        else:
            total += Dict[i] #just straight adds to total
        previous = Dict[i] #marks index as previous
    return total


def rom2int2(R):
    romDict = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } #dictionary
    total =0
    for i in range(len(R)):
        if i < len(R)-1:
            if romDict[R[i]] < romDict[R[i+1]]:
                total -= rom2int2[R[i]]
                continue  #we do not wanna add
        total += romDict[R[i]]
    return total



print(rom2int2("MCCX"))
print(rom2int("MCCX"))
print(rom2int("MCMXCIV"))