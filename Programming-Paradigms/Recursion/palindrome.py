# def palin(n: int, l:int, r : int) -> bool:
#     if l >= r:
#         return True
#     if str(n)[l] != str(n)[r]:
#         return False
#     l += 1 
#     r -= 1 
#     return palin(n,l,r)
# print(palin(22, 0, 1))

def is_palindrome(left: int, right: int, num: int) -> bool:
    if left >= right:
        return True
    elif str(num)[left] != str(num)[right]:
        return False
    else:
        return is_palindrome(left+1, right-1, num)

num = 12321
print(is_palindrome(0, len(str(num))-1, num))

