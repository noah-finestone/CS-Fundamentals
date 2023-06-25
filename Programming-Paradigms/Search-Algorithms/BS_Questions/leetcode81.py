from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            # Handle the case where nums[start] == nums[mid] == nums[end]
            if nums[start] == nums[mid] == nums[end]:
                # In this case, we cannot determine which side is sorted,
                # so we move both start and end towards the center.
                start += 1
                end -= 1
            elif nums[start] <= nums[mid]:
                # The left side is sorted, and we check if the target is within
                # the sorted range. If it is, we update the end pointer to mid - 1,
                # otherwise, we update the start pointer to mid + 1.
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # The right side is sorted, and we check if the target is within
                # the sorted range. If it is, we update the start pointer to mid + 1,
                # otherwise, we update the end pointer to mid - 1.
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False
