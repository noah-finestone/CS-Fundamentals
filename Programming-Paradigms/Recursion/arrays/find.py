# find the index of a target element in a array using recursion 

from typing import List

def find(arr: list, target: int, index: int) -> bool: 
    # base condition
    if index == len(arr) : 
        return False 
    return arr[index] == target or find(arr, target, index+1)


def findAllIndex(arr: list, target: int, index: int, all_indexes: list) -> list: 
    # base condition
    if index == len(arr): 
        return all_indexes
    if arr[index] == target:
        all_indexes.append(index)
    return findAllIndex(arr, target, index+1, all_indexes)
    

    
if __name__ == '__main__': 
    arr = [1,3,4,0,6,6]
    target = 6
    print(findAllIndex(arr, target, 0, []))k


