# skip letter 'a' in string usinf recursion

def skip(new, old): 
    if len(old) == 0:
        print(new)
        return
    if old[0] == 'a':
        #skip
        return skip(new, old[1:])
    else:
        return skip(new + old[0], old[1:])

skip("", "baccdah")
