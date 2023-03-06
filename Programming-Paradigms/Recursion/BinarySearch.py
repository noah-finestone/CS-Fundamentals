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

if __name__ == '__main__': 
    arr = [1,2,3,4,5]
    print(recursiveBS(arr, 3, 0, len(arr)-1))
   
    