# CS1210: QotD21
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
# Write the recursive solution for rom2int().
#
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
# Here, you can assume that the input R is a legal Roman number; in
# other words, if R is illegal, any answer is correct.
#
# Example:
#   >>> rom2int("MCCX")
#   1210
#   >>> rom2int("MCMXCIV")
#   1994
#
values = {'M':1000, 'CM':900, 'D':500, 'C':100, 'XC':90, 'L':50, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
#
def rom2int(R):
    global values
    print(R)
    if len(R) == 0: 
        return 0 
    if len(R) > 1 and R[:2] in values: 
        return values[R[:2]] + rom2int(R[2:]) 
    else: 
        return values[R[0]] + rom2int(R[1:])


print(rom2int("MCCX"))
print(rom2int("MCMXCIV"))
     


         


