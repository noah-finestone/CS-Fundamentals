# function calls, return types, ...
# fact(5) = 5 * fact(4), fact(4) = 4 * fact(3), ... 
# fact(n) = n * fact(n-1)

# fact(5) -> 5 * fact(4) -> 4 * fact(3) -> 3 * fact(2) -> 2 * fact(1)  
# 120 -> 5 * 20 -> 4 * 6 -> 3 * 2 -> 2 * 1

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1) # returning the fxn call!

if '__main__' == __name__:
    print(fact(5))

