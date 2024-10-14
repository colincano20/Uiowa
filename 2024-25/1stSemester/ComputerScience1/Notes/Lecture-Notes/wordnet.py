#assuming words are same length, in specification we are going to assume they are the same length
#def areNeighbors(w1,w2):
 #   count = 0
  #  for i in range(len(w1)):
   #     if w1[i] != w2[i]:
   #         count = count + 1
   # return(count == 1)
### >>> areNeighbors('cat','hat')
#True
### >>> areNeighbors('cat','dog')
# False


#First Attempt
#areNeighbors(w1,w2) returns True if the two words given as
#arguements differ in exactly one letter position. Note that
#this function assumes w1 and w2 are equal length, a condition
#that is emt in the context of this assignment
#
def areNeighbors(w1,w2):
    '''Returns True if w1 and w2 differin exactly 1 letter'''
    count = 0
    #step through words and count mismatched characters
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            if count == 1:    #too many differences
                return (False)
            count = count + 1
#return true if only one difference discovered
    return(count == 1)

#>>>infile = open('words.dat', 'r') #read mode
#>>>S = infile.read()
#>>>len(S)
#34542
#>>> S[0:20]
# 'aargh\nabada\nabaci\nah'
#>>> W = S.split()
#>>> len(W)
#5757
#W[0:4]
#['aargh', 'abaca', 'abaci', 'aback']
#>>> infile.close()


#good programming practice: leading comment describes what the functions are, what it does, and what it returns. It also mentions any explicit assumptions about the contetxt in which the function is to be used

# ''' this is a docstring, used to comment the function within python session
#>>>help(areNeighbors)
#Help on function areNeighbors in module __main__:

#areNeighbors(w1, w2)
 #   Returns True if w1 and w2 differin exactly 1 letter

#note that the docstring on the previous slide is specifed used triple''' rather than the more usual single or double
# ''' is used for a long string, one that can span multiple lines
