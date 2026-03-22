# Why should we use trees? 
# 1. O(logn) searching, add and deleting items
# 2. Ordered storage
#   e.g. In BST, all nodes on the left hand side are lower than the root and all nodes on left side are greater than the root
# 3. Cost efficient

# Searching: 
# Unbalanced binary tree worst case O(n):
    # O
    #  \
    #   O
    #    \
    #     O
    #      ...

# How to solve this problem?
# -> Self-balancing BT

# Where is it used?
# 1. File systems
# 2. Databases
# 3. Network routing
# 4. Maths
# 5. Decision Trees
# 6. Compression of files
# 7. Future data structures (graphs, heaps, ...)

# Binary Tree
#  Node: 
#   (1) Int value 
#   (2) Node left 
#   (3) Node right

# Properties
# 1. Size = total number of nodes
# 2. Child and parent
# 3. Siblings
# 4. Edge: two nodes being connected by a line
# 5. Height: max number of edges between two nodes (that node to the leaf node)
# 6. Leaf nodes: botton nodes
# 7. Level: Subtract height of root - height of node is the level
# 8. Ancestor and descendant
# 9. Degree: number of edges a node has 

# Type of Binary Trees 
# 1. Complete BT: all levels are filled apart from last level (full from left to right)
# 2. Full BT / Strict BT: each node has either 0 or 2 children (no single child)
# 3. Perfect BT: All internal nodes have 2 children and all leafe node are on same level (all levels full)
# 4. Height balanced BT: avg. height O(log n)
# 5. Skewed BT: every node has only 1 child
# 6. Ordered BT: every node has some property (BST for exmaple)

# Properties for some questions:
# 1. Perfect BT, height = h, total nodes = 2**(h+1) - 1
# 2. Perfect BT, total num. leaf nodes = 2**h 
# 3. N = num. of leaves, you'll have log N+1 levels at least
# 4. Strict BT, total leaf nodes = n - 1
# 5. Number of leaf nodes = 1 + num. of interal nodes with 2 children (not incl. root)

#### Implementation ####
# 1. Linked representation
# 2. Sequential -> using array 

class Node:
        def __init__(self, value: int, left=None, right=None):
            self.value = value   # (1) Int value
            self.left = left     # (2) Left child node
            self.right = right   # (3) Right child node

class BinaryTree:
    def __init__(self, root_value: int = None):
        # Initialize tree with optional root node
        self.root = Node(root_value) if root_value is not None else None

    def populate(self, value: int):
        """Insert a value using level-order (BFS) to fill the tree left to right."""
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        # BFS to find the first open spot
        queue = [self.root]
        while queue:
             current = queue.pop(0)
             if not current.left:
                  current.left = new_node
                  return
             queue.append(current.left)
             if not current.right:
                  current.right = new_node
                  return
             queue.append(current.right)
    
    def inorder(self):
        """Kick off the recursive in-order traversal."""
        self._inorder(self.root)

    def _inorder(self, node):
        """Recursive in-order: left -> node -> right."""
        if node is None:            # base case
             return
        self._inorder(node.left)    # visit left subtree
        print(node.value)           # visit node
        self._inorder(node.right)   # visit right subtree

    def display(self):
        """Kick off the recursive display."""
        self._display(self.root, "")
    
    def _display(self, node, indent):
        """Recursively print the tree with indentation."""
        if node is None:
            return
        self._display(node.right, indent + "   ")  # print right side first (top)
        print(indent + str(node.value))             # print current node
        self._display(node.left, indent + "   ")    # print left side (bottom)
        
 
tree = BinaryTree(1)
for v in [2, 3, 4, 5]:
    tree.populate(v)

tree.display()   
