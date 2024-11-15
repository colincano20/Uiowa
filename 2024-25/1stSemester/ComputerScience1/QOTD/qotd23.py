# CS1210: QotD23
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
# Specification: revComp(S) takes a string, S, consisting only of the
# letters 'a', 'c', 'g', and 't' (representing the bases in DNA), and
# returns a new string that represents the "reverse complement" of the
# string S. Your result should always be upper case, and your function
# should be recursive.
#
# Example:
#   >>> revComp('aaaatttggc')
#   'GCCAAATTTT'
#   >>> revComp('acttgagtc')
#   'GACTCAAGT'
#   >>> revComp('acgt')
#   'ACGT'
#
# You can think of DNA as a string of 'a', 'c', 'g' and 't' characters
# where each letter represents a diffferent nucleobase (adenine,
# cytosine, guanine, and thymine, respectively). Strands of DNA are
# twisted together in the familiar double helix arrangement, with
# nucleobases in opposing strands paired according to the Watson-Crick
# base pairing rules (adenine pairs with thymine and cytosine pairs
# with guanine).
#
# Because chemically individual DNA strands are sugar-phosphate
# "backbones," they are in essence "directional." Thus the paired
# backbones:
#   ---> AACGGTAT
#        TTGCCATA <---
# are "read" in opposite directions. As such, these two backbones are
# considered "reverse complements" to one another, where "complement"
# refers to the A/T and C/G pairs, and "reverse" refers to the
# direction in which you read the backbone.
#
def revComp(S):
    D = { 'A':'T', 'C':'G', 'G':'C', 'T': 'A'}
    if len(S) == 0:
        return ""
    return revComp(S[1:]) + D[S.upper()[0]]

print(revComp('aaaatttggc'))
print(revComp('acttgagtc'))
print(revComp('acgt'))
print(revComp("AACGGTAT"))
