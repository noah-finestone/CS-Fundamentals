# count the number of zeros in a number n using recursion 
# F(N, count=0) = if digit = 0 -> F(N//0, count+=1) else F(n//10, count)
# reccurence relation? 

# def count_zeros(n, count):
#     if (n == 0 and count == 0):
#         return 1
#     if (n == 0):
#         return count  
#     if (n % 10 == 0):
#         return count_zeros(n//10, count+1)
#     return count_zeros(n//10, count)

# print(count_zeros(10, 0))





def count_zeros(n, count):
    #12030
    if n == 0 and count == 0: 
        return 1
    if n == 0:
        return count
    if n % 10 == 0:
        return count_zeros(n//10, count+1)
    return count_zeros(n//10, count)


print(count_zeros(1030, 0))















