from typing import List

def countRotatedArray(nums: List[int]) -> int: 
    # find pivot 
    pivot = findPivot(nums)
    # if pivot not last el and pivot is a valid pivot, need to count the amount of numbers behind the pivot + 1
    return pivot + 1  # Pivot is the last element or not a valid pivot, no rotation

def findPivot(nums):
    s = 0
    e = len(nums) - 1

    while s <= e:
        mid = (s + e) // 2 

        if mid < e and nums[mid] > nums[mid + 1]:
            return mid 
        if mid > s and nums[mid] < nums[mid - 1]:
            return mid - 1
        if nums[mid] <= nums[s]:
            e = mid - 1 
        else:
            s = mid + 1
    return -1  

nums = [15, 18, 19, 20, 21, 22]
result = countRotatedArray(nums)
print(result)  # Expected output: 2

