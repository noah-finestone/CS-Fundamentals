# # """
# # This is MountainArray's API interface.
# # You should not implement it, or speculate about its implementation
# # """
# #class MountainArray:
# #    def get(self, index: int) -> int:
# #    def length(self) -> int:
# class Solution:
#     def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
#         peak = self.findPeakElement(mountain_arr)
#         firstTry = self.order_agnostic_BS(target, mountain_arr, 0, peak)
#         if firstTry != -1:
#             return firstTry
#         return self.order_agnostic_BS(target, mountain_arr, peak + 1, mountain_arr.length() - 1)

#     def findPeakElement(self, mountain_arr: 'MountainArray') -> int:
#         s = 0
#         e = mountain_arr.length() - 1

#         while s < e:
#             mid = (s + e) // 2
#             if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
#                 # ascending portion of array
#                 s = mid + 1
#             else:
#                 # descending portion of the array
#                 e = mid
#         return s

#     def order_agnostic_BS(self, target, mountain_arr: 'MountainArray', left: int, right: int) -> int:
#         start = mountain_arr.get(left)
#         end = mountain_arr.get(right)

#         while left <= right:
#             mid = (left + right) // 2
#             middle = mountain_arr.get(mid)

#             if middle == target:
#                 return mid

#             if start < end:
#                 # Array is in ascending order
#                 if middle < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 # Array is in descending order
#                 if middle > target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1
