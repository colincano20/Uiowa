def qsort(L):
    #recursive helper fucntion
    def helper(lo, hi):
        if (lo < hi):
            pivot = L[lo] #pivot value
            mid = lo
            for i in range(lo+1, hi):
                if L[i] < pivot:
                    mid = mid + 1
                    L[i], L[mid] = L[mid], L[i]
            L[lo], L[mid] = L[mid], L[lo] #swap pibot home
            #sort subsequences
            helper(lo,mid)
            helper(mid+1,hi)
    #just call recursive helpeer function, L is private
    helper(0, len(L))
    return(L)
