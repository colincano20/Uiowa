#T = ("Mickey's Back, -12, [3,7,11], "scarlet hillows",)





#5 < P['bush'][0]/7 < 6
True


#T[1]/len(L[3])

#S[36:27:-3



def sandwich(S,i,j,U):
    return(S[:i] + U + S[len(S)-j:])

def uniqueEnd(S):
    return(len(s) > 0 and S[-1] not in S[:-1])

def subsumes(w1, w2):
    return(set(w1.lower()) <= set(w2.lower()) or set(w2.lower()) < set(w1.lower))
        #has its elements contained entirely within the othersets! of lowered letters. Uses set subset, cant use memebership operators

#def vowelRatio(w, alpha=printable[10:36]):
    return((len(set(w.lower()) & set('aeiou'))*100) // (len(set(w.lower()) & set(alpha))))

#takes a string and returns a string that contrains lowercase veriosns of the only uppercase

def spliceUppers(S):
    return(''.join([c.lower() for c in S if c.isupper()]))

def countChars(S):
    return({ c:S.lower().count(c) for c in set(S.lower())})
#countChars("Alberto")        {t:1, 'e': 1

    
    
