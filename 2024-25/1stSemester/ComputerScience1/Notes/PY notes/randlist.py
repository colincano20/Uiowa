import random
import time
import matplotlib.pyplot as plt


#return a randomly ordered list of N numbers between 0 and N-1
def randlist(N):
    return([random.randint(1,N) for i in range(N)])

print(randlist(15))
#Time sort. Note how function is passed as an arguement
def timesort(sort,L):
    start = time.time()
    sort(L)
    return(time.time() - start)


