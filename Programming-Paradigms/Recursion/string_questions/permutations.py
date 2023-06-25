
# find all permutations of a string: 'abc': 'abc', 'acb', 'bac', 'bca', 'cba', 'cab' 

def permutations(new, old):
    if len(old) == 0:
        return [new]  # Return the permutation

    result = []  # List to store permutations

    for i in range(len(new) + 1):
        first = new[:i]
        second = new[i:]
        result += permutations(first + old[0] + second, old[1:])

    return result

print(permutations("", "abc"))





    
    