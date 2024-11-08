# CS1210: Lab9 [2 functions to complete, plus some short answer]
######################################################################
# READ ALL INSTRUCTIONS CAREFULLY.
#
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partner(s), and
#  2) you have not shared it nor will share it with anyone else.
#
# ToDo: Change the two "hawkid" strings to match the hawkids of you
# and your partner(s). Your hawkid is the "login identifier" that you
# use to login to all University services: it is not your email
# address or your student id number.
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "segre". 
#
# Note: if there are 3 of you, add a third string to the list returned
# by signed() below (e.g., change ["hawkid1","hawkid2"] to
# ["hawkid1","hawkid2","hawkid3"], using your own three UI login
# identifiers as the hawkid values).
#
def signed():
    return(["cmcano","tberta"])

######################################################################
# Lab9 has two parts. First complete the two functions below, then go
# to ICON to answer four questions in Lab9quiz.
#
# Note that unlike previous labs, you will need to test your own code:
# the autograder is configured only to check the filename of your
# upload.
######################################################################
# In class, we've studied selection sort as our prototypical O(N^2)
# sorting algorithm. Below is the implementation from 2024-10-21.
#
def selsort(L):
    for i in range(len(L)-1):           # make N-1 passes
        j = i + L[i:].index(min(L[i:])) # note offset i
        L[i],L[j] = L[j],L[i]           # note simultaneous assignment

# There is another common O(N^2) sort called insertion sort. The
# general idea is given a list with the first k elements sorted, take
# the next element and insert it in the right position with respect to
# the first part of the list. So:
#
#   3 | 2 7 5 0 1 4 6    # assume 3 is sorted; insert 2 in order
#   2 3 | 7 5 0 1 4 6    # 2, 3 are sorted; insert 7 in order
#   2 3 7 | 5 0 1 4 6    # 2, 3, 7 are sorted, insert 5 in order
#   2 3 5 7 | 0 1 4 6    # etc.
#   0 2 3 5 7 | 1 4 6
#   0 1 2 3 5 7 | 4 6
#   0 1 2 3 4 5 7 | 6
#   0 1 2 3 4 5 6 7      # done.
#
# Note that insertion sort does not involve just swapping elements;
# instead, we remove an element and insert it into another part of of
# the list. This is a perfect use of slice assignments (not a
# suggestion here, a requirement).
#
def insort(L):
    for i in range(1, len(L)):
        if L[i] >= L[i-1]:
            # Still in sorted portion
            continue # skip loop
        # Will only get to here if the element is not sorted
        for j in range(len(L[:i])):
            if L[i] < L[j]:
                x = L.pop(i)
                L[:] = L[:j] + [x] + L[j:]
                break
def insort2(L):
    for i in range(1,len(L)):
        j = 0
        while j < i and L[j] < L[i]:
            j += 1
        L[i:i+1], L[j:j] = [], [L[i]] #swap

# L = [3, 2, 7, 5, 0, 1, 4, 6]
# insort(L)
# # print(L)
######################################################################
# In QotD17 and QotD18 we worked on merge(L1, L2) where L1 and L2 are
# lists of numbers in sorted order; your function should return a new
# list containing all of the elements in L1 and L2 still in order.
#
# As we discussed in class, we can make use of the merge(L1, L2)
# function to implement merge sort. Merge sort is an O(N log N)
# sorting algorithm that makes use of extra space to get to that kind
# of run time. I'll include my solution to merge(L1, L2) as a helper
# function.
#
# Because merge sort is not in-place, you'll need to make sure, unlike
# insort(), selsort(), or qsort(), to return the result of msort().
#
# >>> L=list(range(10))
# >>> L
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> shuffle(L)
# >>> L
# [9, 3, 5, 7, 2, 6, 1, 0, 4]
# >>> msort(L)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Your solution should be recursive, consisting of a base case and a
# recursive step.
#
def msort(L):
    def merge(L1, L2):
        result = []
        i = j = 0
        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                result.append(L1[i])
                i = i+1
            else:
                result.append(L2[j])
                j = j+1
        return(result + L1[i:] + L2[j:])
    
    if len(L) <= 1:
        return L

    return merge(msort(L[:len(L)//2]), msort(L[len(L)//2:]))
def msort2(L):
    def merge(L1, L2):
        result = []
        i = j = 0
        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                result.append(L1[i])
                i = i+1
            else:
                result.append(L2[j])
                j = j+1
        return(result + L1[i:] + L2[j:])
    if len(L) < 2:
        return(L)
    return(merge(msort(L[:len()//2]), msort(L[len(L)//2:])))

    

# print(msort([9, 3, 5, 7, 2, 6, 1, 0, 4]))  
