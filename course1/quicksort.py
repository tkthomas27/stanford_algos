
# test sizes
# size first last median
# 10 25 29 21
# 100 615 587 518
# 1000 10297 10184 8921

# ---------------------------------------------------------------------

# read in data
intarray_raw = ("/Users/kthomas1/github/stanford_algos/course1/quicksort_t2.txt")
intarray_open = open(intarray_raw, 'r')
with intarray_open as f:
    intarray = [int(integers.strip()) for integers in f.readlines()]

intarray1 = intarray
intarray2 = list(reversed(intarray))
intarray3 = intarray

# ---------------------------------------------------------------------

# pivot first element
def partition(A,l,r):
    i = l
    p = A[i]
    for j in range (l+1,r+1):
        if A[j] < p:
            i = i+1
            A[j], A[i] = A[i], A[j]
    A[i], A[l] = A[l], A[i]
    
    return i 

def quicksort(A,l,r):
    global ml 
    ml = ml+r-1
    if l<r:
        i = partition(A,l,r) # partition
        quicksort(A,l,i-1) # quicksort first partition
        quicksort(A,i+1,r) # quicksort second partition
    return A, ml

ml=0
sorted_array1, ml = quicksort(intarray1,0,len(intarray1)-1)

# ---------------------------------------------------------------------

# # pivot last element
# def partition(A,l,r):
#     i = l
#     p = A[i]
#     for j in range (l+1,r+1):
#         if A[j] < p:
#             i = i+1
#             A[j], A[i] = A[i], A[j]
#     A[i], A[l] = A[l], A[i]
#     return i 

# def quicksort(A,l,r):
#     global mr
#     mr = mr+r-1 #count comparisons
#     if l<r:
#         i = partition(A,l,r) # partition
#         quicksort(A,l,i-1) # quicksort first partition
#         quicksort(A,i+1,r) # quicksort second partition
#     return A, mr

# mr=len(intarray2)
# sorted_array2, mr = quicksort(intarray2,0,len(intarray2)-1)

# ---------------------------------------------------------------------

# pivot random element

# ---------------------------------------------------------------------

print(ml)




















