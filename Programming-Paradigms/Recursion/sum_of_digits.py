# n = 1342 -> 1+3+4+2
# do this recursivly

def sum(n):
    if n == 0:
        return 0
    return (n%10) + sum(n//10)

print(sum(1342))