def fun(n): 
    if n == 0:
        return
    else:
        print(n)
        fun(n-1)
fun(8)

def funRev(n): 
    if n == 0:
        return
    else:
        funRev(n-1)
        print(n)

# time complexity: O(n)
# space complexity: O(n)