# Print all combinations of numbers from 1 to `n` having sum `n` using recursion


# Recursive function to print all combinations of numbers from `i` to `n`
# having sum `n`. The `index` denotes the next free slot in the output list `out`
def printCombinations(i, n, out, index):
    if n == 0:
        print(out[:index])
        return
    # start from the previous element in the combination till `n`
    for j in range(i, n + 1): 
        out[index] = j

        # recur with a reduced sum
        printCombinations(j, n - j, out, index + 1)
        
def print_combinations(n, current_combination=[]):
    if n == 0:
        print(current_combination)
        return

    for num in range(1, n + 1):
        if not current_combination or num >= current_combination[-1]:
            updated_combination = current_combination + [num]
            print_combinations(n - num, updated_combination)

n = int(input("Enter a positive integer (n): "))
print_combinations(n)

# if __name__ == '__main__':
 
#     n = 3
#     out = [None] * n
 
#     # print all combinations of numbers from 1 to `n` having sum `n`
#     printCombinations(1, n, out, 0)
    
