# arr = [18, 12, -7, 3, 14, 28]
# Q: search for 3 in the range [1,4]

def linearSearch(arr: list, target: int, start: int, stop: int):
    if len(arr) == 0 or start >= len(arr) or stop >= len(arr):
        return -1
    if len(arr) == 0:
        return -1
    for i in range(start, stop+1):
        # check for el in at every index if its == target
        if arr[i] == target:
            return i 
    # if non of above return statements above execute, target not found
    return -1 

if __name__ == '__main__': 
    arr = [18, 12, -7, 3, 14, 28] 
    target = 14
    print(linearSearch(arr, target, 1, 4))