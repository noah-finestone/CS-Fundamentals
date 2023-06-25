# what if we are given an infinite array? 
# How do we search for a target number in this inf array?

# Firstly try BRUTE FORCE: start at idx 0, keep going until u find target -> linear search log(n)
# We know it sorted... apply BS obviously but we dont know the start and end of the array
# Check chunk by chunck 

def search_infiniteArray(nums, target):
    l = 0 
    r = 1
    while (target > nums[r]):
       new_l = r + 1      
       r = r + 2 * (l - r + 1)   # 1hr:53mins "Binary Search Interview Questions - Google, Facebook, Amazon" on ytb
       l = new_l
 
    return binarySearch(nums, l, r, target)

def binarySearch(arr, l, r, target):
    start = l
    end = r

    while start <= end: 
        mid = (end + start) // 2 

        if arr[mid] == target:
            return mid 
        if arr[mid] > target: 
            end = mid - 1
        if arr[mid] < target: 
            start = mid + 1 

    return -1 

# Test case
nums = [1, 3, 5, 7, 9, 11, 13]
target = 71

result = search_infiniteArray(nums, target)
print(result)