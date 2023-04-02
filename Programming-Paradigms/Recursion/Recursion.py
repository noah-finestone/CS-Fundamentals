# Why recursion?: 
#   1) It helps us in solving bigger/complex problems in a simple way 
#   2) You can convert recursive solutions into iterative solutions and vice versa
#   3) Space complexity is not constant because of recursive calls
#   4) Helps us in breaking down bigger problems into smaller ones 

# Two types of recursion:
#   Tail-recursive: If the recursive call occurs at the end of a method, it is called a tail recursion
#   Head-recursive: If the recursive call occurs at the beginning of a method, it is called a head recursion.

# Types of reccurence relations: 
#   Linear reccurence relation -> Fibonacci (search space is reduced linearly)
 
# Approaching a problem:
#   1) Identify if you can break down the problem into smaller problems
#   2) Write the recurrence relation if needed
#   3) Draw the recursive tree
#   4) About the tree: 
        # See flow of fxns, how they are put into stack
        # Identify flow of left tree and right tree calls
        # Draw the tree and pointers again and again using pen and paper (or debugger)
#   5) See how values are returned at each step, see where two fxn calls will come out of
#       (in the end you will come out of the main fxn)

#### TIP ###:   DO NOT OVERTHINK!