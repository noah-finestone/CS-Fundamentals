##### Find the nth fibonacci number #####

# Notes: 
# If the solution has a recurrence relation you can use recursion 
# * Break it down into smaller problems
# * The bas condition is represented by answers we already have
# Recurence relation: fib(n) = fib(n-1) + fib(n-2) 
# Recursive Tree: 
#               fib(4)
#             /        \
#          fib(3)  +    fib(2)
#         /     \      /      \
#      fib(2) + fib(1) fib(1) + fib(0)
#      /    \
#  fib(1) + fib(0)

def fibo(n):
    if n < 2: 
        return n  
    return fibo(n-1) + fibo(n-2)

# stack: [main(), fib(4), fib(3), fib(2), fib(1)] -> 1
# stack: [main(), fib(4), fib(3), fib(2), fib(0)] -> 0
# stack: [main(), fib(4), fib(3), fib(2)] -> fib(2) = 1
# stack: [main(), fib(4), fib(3), fib(1)] -> fib(1) = 1
# stack: [main(), fib(4), fib(3)] -> fib(3) = 2
# stack: [main(), fib(4), fib(2), fib(1)] -> 1
# stack: [main(), fib(4), fib(2), fib(0)] -> 0
# stack: [main(), fib(4), fib(2)] -> fib(2) = 1
# stack: [main(), fib(4)] -> fib(3) + fib(2) = 3
# stack: [main()]
# stack: []

if __name__ == '__main__': 
    print(fibo(4))