class Solution:
    def searchRange(self, nums, target):
        s = 0  # Start index of the search range
        e = len(nums) - 1  # End index of the search range

        while s <= e:
            mid = (s + e) // 2  # Calculate the middle index

            if target < nums[mid]:  # If the target is less than the middle element
                e = mid - 1  # Adjust the end index to search in the left half
            elif target > nums[mid]:  # If the target is greater than the middle element
                s = mid + 1  # Adjust the start index to search in the right half
            else:  # If the target is equal to the middle element
                if nums[s] != target:  # Check if the start element is not equal to the target
                    s = s + 1  # Adjust the start index to search for the first occurrence of the target
                elif nums[e] != target:  # Check if the end element is not equal to the target
                    e = e - 1  # Adjust the end index to search for the last occurrence of the target
                else:  # If both start and end elements are equal to the target
                    return [s, e]  # Return the indices of the first and last occurrence of the target

        return [-1, -1]  # Return [-1, -1] if the target is not found in the array
    
solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = solution.searchRange(nums, target)
print(result)  # Output: [3, 4]

###OR###

class Solution:
    def searchRange(self, nums, target):
        start = self.search(nums, target, True)
        end = self.search(nums, target, False)

        return [start, end]

    def search(self, nums, target, searchStart):
        s = 0
        e = len(nums) - 1

        ans = -1

        while s <= e: 
            mid = (s + e) // 2

            if target < nums[mid]: 
                e = mid - 1 
            elif target > nums[mid]: 
                s = mid + 1
            else: 
                ans = mid 
                # search start index 
                if searchStart: 
                    e = mid - 1 
                else:
                    # search end index 
                    s = mid + 1 
        return ans 
