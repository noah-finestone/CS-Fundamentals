# 1. if arr[s] <= arr[mid] then left is sorted 
        # if key >= arr[s] and <= arr[mid]
        # end = mid-1
    #    else s = mid+1 
# 2. if key >= mid and <= end then search in that range
#       s = mid + 1 
#       else e = mid - 1

def search(arr, target, s, e): 
    if (s > e):
        return -1 
    
    m = s+e//2
    if arr[m] == target:
        return m 
    
    if arr[s] <= arr[m]: 
        if target >= arr[s] and target <= arr[m]: 
            return search(arr, target, s, m-1)
        else:
            return search(arr, target, m+1, e)
        
    if target >= arr[m] and target <= arr[e]:
        return search(arr,target,m+1, e)
    return search(arr,target,s, m-1)

arr = [5,6,7,8,9,1,2,3]
print(search(arr, 8, 0, len(arr)-1))