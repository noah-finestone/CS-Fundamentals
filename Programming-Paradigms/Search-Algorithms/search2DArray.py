

def search2DArray(arr: list, target: int):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
          if arr[i][j] == target:
              return i,j
    return -1   

def maxSearch2DArray(arr: list):
    maxi = float('-inf')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
          if arr[i][j] > maxi:
              maxi = arr[i][j]
    return maxi 






if __name__ == '__main__': 
    target = 56
    arr = [[23, 4, 1],
           [18, 12, 3, 9],
           [78, 99, 34, 56],
           [18, 12]]
    print(maxSearch2DArray(arr))