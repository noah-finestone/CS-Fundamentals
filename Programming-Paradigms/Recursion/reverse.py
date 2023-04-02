import math
# TAKE AWAY: 
# 1.To find the number of digits in a n: floor(log10(n)) + 1 
# 2. To get last digit of a n: n%10
# 3. // is a floor division operator in Python. It performs division and returns the whole number (quotient) without the remainder (an int).



# n = 12345 -> 54321
# n = 1824 -> 4281
# do this recursively 

# tree: f(1824) -> "4" + f(182)
#                           -> f(18) + "2"
#                                  -> f(1) + "8"
#                                        -> f() + "1"

# reccurence relation: F(N) = (N%10) add F(N//10)

def rev1(n, reversed_num=0): 
    if n == 0:
        return reversed_num
    reversed_num = (reversed_num * 10) + (n % 10)
    return rev1(n // 10, reversed_num)

print(rev1(1234))

# F(N, args) = (N%10) * (10^args-1) + F(N//10, args-1)

def rev2(n): 
    digits = math.floor(math.log10(n)) + 1 
    return helper(n, digits)

def helper(n, digits):
    if (n%10 == n):
        return n 
    return (n%10) * int(math.pow(10, digits-1)) + helper(n//10, digits-1) 

print(rev2(1234))


    
    