# Traversal methods

# 1. Pre-order: N -> L -> R
# 2. In-order: L -> N -> R * printing BST in increasing order
# 3. Post-order: L -> R -> N * delete binary tree (take care of children first)

# BFS (Breadth-First Search):
# → Level-by-level traversal using a queue.

# DFS (Depth-First Search):
# → Go as deep as possible first (left/right), using recursion or a stack.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self, node):
        if node is None:
            return
        
        print(node.value)                 # visit root
        self.preorder(node.left)          # left
        self.preorder(node.right)         # right

    def postorder(self, node):
        if node is None:
            return
        
        self.postorder(node.left)         # left
        self.postorder(node.right)        # right
        print(node.value)                 # visit root

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    print("Preorder:")
    root.preorder(root)

    print("Postorder:")
    root.postorder(root)