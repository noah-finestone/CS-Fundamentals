# how do we apply binary search if we dont know if array is in descneding or ascending order? 
# order-agnostic binary search 
# well.... simply compare first and last element

def order_agnostic_BS(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] < arr[right]:
            # Array is in ascending order
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # Array is in descending order
            if arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1

    return -1
 
        
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 8
    print(order_agnostic_BS(arr, target))