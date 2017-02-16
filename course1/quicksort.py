
x = [3,1,4,8,5,6,7]

# pivot element 1

def quicksort(A, n):
    
    if n=1: return A
    
    p = ChoosePivot(A,n)
    
    partition(A,l,r):
        p = A[l]
        i = l+1
        j = l+1
        for j in range (j,r):
            if A[j] < p:
                A[j] = A[i]
                i = i+1
        A[l] = A[i-1]
    
    Recursively Sort 1st part
    
    Recursivley Sort 2nd part



def partition(A,l,r):
    p = A[l]
    i = l+1
    j = l+1
    for j in range (j,r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]
    
    return A

x = [3,8,2,5,1,4,7,6]

partition(x,0,len(x))





