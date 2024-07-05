# given a str return all subsets of the string

# str = "abc" return ans = ["a", "b", "c", "ab", "ac", "bc", "abc"]
# the pattern of taking some elements and removing some is the "Subset pattern"

def subseq(p, up): 
    if up == "":
        print(p)
        return
    
    char = up[0]
    subseq(p + char, up[1:])
    subseq(p, up[1:])

def subseq2(p, up, result=[]):
    if up == "":
        result.append(p)
        return
    
    char = up[0]
    subseq2(p + char, up[1:], result)
    subseq2(p, up[1:], result)
    
    return result

# Example usage:
up = "abc"
result = subseq2("", up)
print(result)


 

