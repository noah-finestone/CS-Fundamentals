# -----------------------------
# AVL Tree Notes 
# -----------------------------

# 1. What is an AVL Tree?
# - AVL tree is a type of Binary Search Tree (BST)
# - It is self-balancing
# - Balance rule: For any node, height(left subtree) - height(right subtree) <= 1
# - If a node becomes unbalanced after insertion/deletion, we rotate to fix it
# - Rotations: Left, Right, Left-Right, Right-Left
# - Searching, inserting, deleting: O(log n) time

# 2. Problem with regular BSTs
# - If nodes are inserted in sorted order, BST can become unbalanced
# - Worst-case: a “chain” or skewed tree
#       O
#        \
#         O
#          \
#           O
#            ...
# - Height = n → operations degrade to O(n)

# 3. Definition of a balanced tree (AVL condition)
# - For every node in the tree:
#       balance_factor = height(left_subtree) - height(right_subtree)
# - Balance factor must be -1, 0, or +1
#       -1 ≤ balance_factor ≤ 1
# - Ensures the tree is roughly balanced → O(log n) height

# 4. Solution
# - Use a self-balancing BST, e.g., AVL tree
# - Automatically performs rotations during insertions/deletions to maintain balance
# - Keeps operations fast even in worst-case scenarios
# __________________________________________________________________

# -----------------------------
# AVL Tree Insertion Algorithm
# -----------------------------

# 1. Insert a new node normally (like a regular BST). Call this node `x`.

# 2. After insertion, traverse back from `x`
#    to find the first ancestor node that becomes unbalanced.
#    Let’s call this node `p` (the first unbalanced ancestor).

# 3. Identify the child of p (call it `c`) that is on the path to `x`.
#    Identify the grandchild `g` (child of `c`) on the path to `x`.

# 4. Use one of the four AVL rotation rules (LL, RR, LR, RL) to rebalance.

# -----------------------------
# Example of an unbalanced subtree
# -----------------------------
#         p          <- first unbalanced node
#       /   \
#      c     t4      <- c = child of p on path to x, t4 = other subtree
#     / \
#    g   t3           <- g = grandchild on path to x
#   / \
#  t1  t2
# x = inserted node somewhere in g’s subtree (or g itself)

# -----------------------------
# AVL Tree Rotation Cases (explicit inserted node x)
# -----------------------------

# Legend:
# p = parent of unbalanced subtree
# c = child of p (on insertion path)
# g = grandchild (child of c on insertion path, may contain x)
# x = newly inserted node
# t1, t2, t3, t4 = other subtrees

# -----------------------------
# Case 1: Left-Left (LL)
# -----------------------------
# Insertion happened in left subtree of left child (x is in g's left subtree)
# Solution: Right rotation at p

# Before rotation:
#         p
#       /   \
#      c     t4
#     / \
#    g   t3
#   / \
#  t1  t2
# x = somewhere in g's left subtree

# Right rotation around p:

#         c
#       /   \
#      g     p
#     / \   / \
#   t1  t2 t3  t4
# x stays in g’s subtree

# -----------------------------
# Case 2: Right-Right (RR)
# -----------------------------
# Insertion happened in right subtree of right child (x is in g's right subtree)
# Solution: Left rotation at p

# Before rotation:
#         p
#       /   \
#     t4     c
#           / \
#         t1   g
#             / \
#           t2  t3
# x = somewhere in g's right subtree

# Left rotation around p:

#         c
#       /   \
#      p     g
#     / \   / \
#   t4  t1 t2  t3
# x stays in g’s subtree

# -----------------------------
# Case 3: Left-Right (LR)
# -----------------------------
# Insertion happened in right subtree of left child (x is in g's right subtree)
# Solution: Left rotation at c, then right rotation at p

# Before rotations:
#         p
#       /   \
#      c     t4
#     / \
#   t1    g
#        / \
#      t2   t3
# x = somewhere in g's right subtree

# Step 1: Left rotation on c:

#         p
#       /   \
#       g     t4
#     /  \
#    c    t3
#   / \
# t1  t2

# Step 2: Right rotation on p:

#         g
#       /   \
#      c     p
#     / \   / \
#   t1  t2 t3  t4
# x stays in g’s subtree

# -----------------------------
# Case 4: Right-Left (RL)
# -----------------------------
# Insertion happened in left subtree of right child (x is in g's left subtree)
# Solution: Right rotation at c, then left rotation at p

# Before rotations:
#         p
#       /   \
#     t4     c
#           / \
#          g   t3
#         / \
#       t1  t2
# x = somewhere in g's left subtree

# Step 1: Right rotation on c:

#         p
#       /   \
#     t4      g
#           /   \
#          t1    c
#               / \
#             t2  t3

# Step 2: Left rotation on p:

#         g
#       /   \
#      p     c
#     / \   / \
#   t4  t1 t2  t3
# x stays in g’s subtree

# -----------------------------
# Summary:
# - After BST insertion of x, check balance factor bottom-up
# - If unbalanced:
#     - LL → right rotation on p
#     - RR → left rotation on p
#     - LR → left rotation on child + right rotation on parent
#     - RL → right rotation on child + left rotation on parent
# - Heights updated after rotation
# - g represents the node on the path to x used in rotation diagrams

# Node structure
class Node:
    def __init__(self, value):
        self.value = value   # Value stored in the node
        self.left = None     # Left child
        self.right = None    # Right child
        self.height = 1      # Height of node (leaf node = 1)

# AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    # Utility: get height of node
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Utility: get balance factor of node
    # balance = height(left) - height(right)
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotate
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        # Return new root
        return y

    # Left rotate
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        # Return new root
        return y

    # Insert node recursively
    def insert(self, node, value):
        # 1. Normal BST insert
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # 2. Update height of this ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 3. Get balance factor to check if unbalanced
        balance = self.get_balance(node)

        # 4. If unbalanced, there are 4 cases

        # Case 1 - Left Left
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the (unchanged) node pointer
        return node

    # Helper to insert value starting from root
    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    # Display tree in-order (left, root, right)
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right) 
