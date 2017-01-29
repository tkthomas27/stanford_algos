
# inspired by
# http://www.shawnohare.com/2013/08/counting-inversions-in-python.html
# https://pythonandr.com/2015/07/20/number-of-inversions-in-an-unsorted-array-python-code/
# http://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort
# http://www.cs.cmu.edu/~ckingsf/class/02713-s13/lectures/lec12-inversions.pdf
# http://www.cs.princeton.edu/~wayne/cs423/lectures/divide-and-conquer-4up.pdf
# https://people.cs.umass.edu/~sheldon/teaching/mhc/cs312/2013sp/Slides/Slides13%20-%20Counting%20Inversions.pdf
# https://www.cs.umd.edu/class/fall2009/cmsc451/lectures/Lec08-inversions.pdf


# import array
intarray_raw = ("/Users/kthomas1/github/stanford_algos/course1/integerarray.txt")
intarray_open = open(intarray_raw, 'r')
with intarray_open as f:
    intarray = [int(integers.strip()) for integers in f.readlines()]

def sortcount(A, count):

    # base case
    if len(A)==1:
        return 0,A
    
    # divide
    half = int(len(A)/2)
    B = A[:half]
    C = A[half:]
    
    # conquer
    X, B = sortcount(B, count)
    Y, C = sortcount(C, count)
    Z, D = mergecount(B, C, count)
    
    # get results
    inv_ct = X+Y+Z
    return inv_ct, D
    
def mergecount(B, C, count):
    
    # initialize blank list
    outlist = []

    # sort and count
    while B and C:
        if B[0] <= C[0]:
            outlist.append(B.pop(0))
        else:
            count += len(B)
            outlist.append(C.pop(0))

    # compute total 
    outlist += B + C
    return count, outlist

# print results
inversions, sorted_array = sortcount(intarray, count=0)
print(inversions)


