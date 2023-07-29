class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        s = 0 
        e = len(arr) - 1

        while s < e:
            mid = (s+e) // 2

            if arr[mid] < arr[mid+1]: 
                # ascending portion of array
                s =  mid + 1 
            else:
                # descending portion of the array 
                e = mid 

        return s
    
    [1, 2, 3, 5, 4, 2, 1]
