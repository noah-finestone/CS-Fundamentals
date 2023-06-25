def findMin(arr: list):
    answer = arr[0]
    # return the min value in array
    for i in range(1, len(arr)):
        if arr[i] < answer:
            answer = arr[i]
    return answer 
     


if __name__ == '__main__': 
    arr = [18, 12, -7, 3, 14, 28]
    print(findMin(arr))