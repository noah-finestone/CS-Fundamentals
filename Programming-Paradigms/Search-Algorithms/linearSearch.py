# Linear search is a simple searching algorithm used in data structures and algorithms. 
# It sequentially checks each element in a given list or array until it finds the desired target value. 
# Starting from the beginning, it compares each element with the target, and if a match is found, it returns 
# the index of that element. If the entire list is traversed without finding the target, it returns a specified 
# value to indicate the absence of the target. Linear search is straightforward to implement but 
# can be inefficient for large datasets, as it has a time complexity of O(n), where n represents 
# the number of elements in the list.


# Given an array of numbers, find whether a number exists in the array or not
# Solution: for each loop or use indexes 
# Time complexity: Best -> O(1), Worts -> O(N)

# arr = [18, 12, 9, 14, 77, 50]

# search in the array: return the index if item found else -1 
def linearSearch(arr: list, target: int):
    if len(arr) == 0:
        return -1
    for i in range(len(arr)):
        # check for el in at every index if its == target
        if arr[i] == target:
            return i 
    # if non of above return statements above execute, target not found
    return -1 

def linearSearchString(string: str, char: chr):
    if len(string) == 0:
        return -1
    for i in range(len(string)):
        # check for el in at every index if its == target
        if string[i] == char:
            return i 
    # if non of above return statements above execute, target not found
    return -1 

if __name__ == '__main__': 
    arr = [18, 12, 9, 14, 77, 50]
    target = 777
    print(linearSearch(arr, target))
    string = 'Noah'
    char = 'h'
    print(linearSearchString(string, char))

