from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num, 0)
    
    def helper(self, num, count): 
        if num == 0:
            return count 
        else: 
            if (num % 2) == 0:
                # even
                return self.helper(num/2, count+1)
            else:
                # odd 
                return self.helper(num-1, count+1)