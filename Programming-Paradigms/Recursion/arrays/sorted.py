# find if array is sorted or not using recursion 
from typing import List

def sorted(arr: list, indx: int) -> bool: 
    # base condition
    if indx == len(arr) - 1: 
        return True 
    elif arr[indx] <= arr[indx+1]: 
        return sorted(arr, indx+1)
    else:
        return False 
    
if __name__ == '__main__': 
    arr = [1,3,4,6,5]
    indx = 0
    print(sorted(arr, indx))


