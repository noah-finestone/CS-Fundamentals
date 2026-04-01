# Iterate over the tree level by level
# When to use this:
#   1. When answer lies near the root
#   2. When you are asked to search by level (doing ops level-wise)


# Start with root node (via every node I can access its children)
# Use a queue to store the nodes in order, priting the node and then adding the nodes children to the queue

# Time complexity: O(n)
# Space complexity: 

#  Leetcode question 102. Binary Tree Level Order Traversal

# Define the structure for a binary tree node
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_level_order(root: TreeNode):
    result = []

    if not root:
        return result
    
    queue = [] 
    queue.append(root)

    while queue:
        levelSize = len(queue) 
        currentLevel = []

        for _ in range(levelSize):
            currentNode = queue.pop(0)
            currentLevel.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    print(result)
    return result 

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
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    

    # Print the tree level by level
    print_level_order(root)
