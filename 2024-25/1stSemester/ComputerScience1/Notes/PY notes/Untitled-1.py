

def countExtraS(S):
    return(len(S) - len(set(S)))
def countExtras2(S):
    count = 0
    for i in range(len(S) - 1):
        if S[i] in S[:i]:
            count += 1
    return count

print(countExtraS((1,2,3,4,5,1,1,2,2,4)))
print(countExtras2((1,2,3,4,5,1,1,2,2,4)))

def peak(S):
    count = 0
    for i in range(len(S)-1):
        if S[i] >= S[i-1] and S[i] > S[i+1]:
            count += 1
    if S[-1] >= S[-2] and S[-1] > S[0]:
            count +=1
    return count

def peak2(S):
    count = 0
    for i in range(len(S)):
        if S[i-1] <= S[i] >  S[(i+1) %len(S)]:
            count += 1
    return count


print(peak2('AaBbCcDd'))
print(peak2((1,7,2,4,3,5,6,7,2)))



def stringify(S, c='.'):
    if isinstance(S,(list,tuple,set,range)):
        return(c.join([stringify(e,c) for e in S if S != '']))
    return str(S)


print(stringify((1,2,3,4,5), c='.'))

def findExtras(S,skip=()):
    if len(S) <= 1:
        return(set())
    result = findExtras(S[1:],skip)
    if S[0] not in skip and S[0] in S[1:]:
        result.add(S[0])
    return(result)

def extraR2(S,skip=()):
    S = list(S) #S.split()
    if len(S) == 0:
        return set()
    result = set()
    if S[0] not in skip and S[0] in S[1:]:
        result.add(S[0])
    return(result.union(extraR2(S[1:], skip)))


print(findExtras([1,2,3,4,5,1,1,2,2,4]))
print(findExtras('the timmy is mirac', ('the',)))


