# Binary search is an efficient searching algorithm commonly used in data structures and algorithms. 
# It relies on the concept of divide and conquer. The algorithm works by repeatedly dividing the "sorted" list or array 
# into halves and comparing the target value with the middle element. If the target is equal to the middle element, 
# the search is successful, and the index is returned. If the target is smaller, the search continues in 
# the lower half, or if the target is larger, the search continues in the upper half. 
# By iteratively narrowing down the search range, binary search quickly converges towards the target. 
# This algorithm has a time complexity of O(log n), where n represents the number of elements in the sorted list.
# Binary search is highly efficient for large datasets and is commonly used in scenarios where the data is sorted.

# Best case: O(N)
# Worst case: O(log(N)) 


# array must be sorted!!

# Steps: 1. find the middle element and compare to target 
#        2. if target > middle el, search right side else search left
#        3. if middle == target return its index 

# return the index else return -1
def binarySearch(arr, target):
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

    return -1 
        
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 1
    print(binarySearch(arr, target))




