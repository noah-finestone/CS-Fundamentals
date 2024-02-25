# print all subsets of a list 

def subset(arr):
    outer = [[]]

    for num in arr:
        n = len(outer)
        for i in range(n):
            subset_copy = outer[i].copy()
            subset_copy.append(num)
            outer.append(subset_copy)

    return outer

def subsetDuplicates(arr):
    outer = [[]]
    s = 0 
    e = 0

    for i in range(len(arr)):
        s = 0
        if i > 0 and arr[i] == arr[i-1]:
            s = e + 1 
        e = len(outer) - 1

        n = len(outer)
        for j in range(s, n):
            subset_copy = outer[j].copy()
            subset_copy.append(arr[i])
            outer.append(subset_copy)

    return outer
# when you find a duplicated element only add it in the newly created subset
# of the previous step, what if 2,1,2...  sort arr

if __name__ == "__main__":
    example_input = [1, 2, 2]
    result = subsetDuplicates(example_input)
    print("Input List:", example_input)
    print("All Subsets:", result)