# Lets create a function to print the nodes level by level
from collections import deque

# Define the structure for a binary tree node
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_level_order(root):
    if not root:
        return

    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        # Process all nodes at the current level
        for i in range(level_size):
            node = queue.popleft()
            print(node.value, end=' ')
            
            # Enqueue left child
            if node.left:
                queue.append(node.left)
            
            # Enqueue right child
            if node.right:
                queue.append(node.right)
        
        # Move to the next level
        print()  # Newline after each level

# Example usage
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Print the tree level by level
    print_level_order(root)
