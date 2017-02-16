
def partition(A,l,r):
    p = A[l]
    i = l+1
    j = l+1
    for j in range (j,r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]
    
    return A, i

x = [3,8,2,5,1,4,7,6]

aa = partition(x,0,len(x))















# pivot element 1

def partition(A,l,r):
    p = A[l]
    i = l+1
    j = l+1
    for j in range (j,r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]
    
    return i

def quicksort(A,l,r):
    
    if l<r:
    
        # parittion
        i = partition(A,l,r)
        
        quicksort(A,l,i-1)
        quicksort(A,i+1,r)


x = [54,26,93,17,77,31,44,55,20]
quicksort(x,0,len(x))
x






