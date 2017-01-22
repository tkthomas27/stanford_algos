
# inspired by https://en.wikipedia.org/wiki/Karatsuba_algorithm
# debugged using http://stackoverflow.com/questions/15860257/karatsuba-algorithm-incorrect-result

def karatsuba( num1, num2 ):
    
    if min(num1, num2) < 10:
        return num1 * num2
    
    # lengths
    l = len(str(num1))
    m = int(l/2)
    
    # divide
    def divide(x):
        # // 10 ** m --> will grab the first m digits
        # % 10 ** m --> will grab the last m digits
        return x // 10 ** m, x % 10 ** m

    x1, x0 = divide(num1)
    y1, y0 = divide(num2)

    # conquer
    # recursively call karatsuba to reduce multiplication problem to smallest problems
    z2 = karatsuba(x1,y1)
    z0 = karatsuba(x0,y0)
    z1 = karatsuba(x1+x0,y1+y0) - z2 - z0

    solution = z2 * 10**(2*m) + z1 * 10**m + z0
    return solution

