# ceiling = smallest el in array >= target
# Q: find a number >= my target element 


# return idx of smallest no >= target
def ceiling_binarySearch(arr, target):
    start = 0 
    end = len(arr) - 1 

    while start <= end: 
        mid = (end + start) // 2 

        if arr[mid] == target:
            return mid 
        if arr[mid] > target: 
            end = mid - 1
        if arr[mid] < target: 
            start = mid + 1 
    if start >=0 and start < len(arr):
        return start 
    return -1 

        
if __name__ == '__main__': 
    arr = [1, 3, 5, 7, 9, 10]
    target = 6
    print(ceiling_binarySearch(arr, target))