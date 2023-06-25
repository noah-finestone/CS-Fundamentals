##### Implement binary search using recursion #####

def recursiveBS(arr, target, l, r): 
    if l > r: 
        return -1  
    m = (l+r) // 2

    if arr[m] == target:
        return m
    if target < arr[m]:
        return recursiveBS(arr, target, l, m-1)
    return recursiveBS(arr, target, m+1, r)

# if __name__ == '__main__': 
#     arr = [1,2,3,4,5]
#     print(recursiveBS(arr, 1, 0, len(arr)-1))
#     print(1//2)
   
    # time complexity: O(log n)
    # space complexity: O(log n)
    # recurrence relation: F(N) = O(1) + F(n/2)

def rec_bs(arr, target, s, e): 
    if s > e:
        return -1 
    mid = (s+e)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target: 
        return rec_bs(arr,target,s,mid-1)
    return rec_bs(arr,target,mid+1,e)

print(rec_bs([1,2,3,4,5], 7, 0, 4))
