# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        Return the in-order successor of node p.
        """
        if not root:
            return None
        if root.val > p.val:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            return root
        else:
            return self.inorderSuccessor(root.right, p)
        
# Time is O(h), space is O(h), which is O(log n) for balanced trees and O(n) in the worst case.



# -----------------------------
# Helper Functions (for testing)
# -----------------------------

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def build_bst(values):
    root = None
    for v in values:
        root = insert_into_bst(root, v)
    return root


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Build BST: [6, 3, 8, 1, 4, 10]
    values = [6, 3, 8, 1, 4, 10]
    root = build_bst(values)

    # Test cases
    test_vals = [3, 4, 6, 10]

    for val in test_vals:
        p = find_node(root, val)
        successor = sol.inorderSuccessor(root, p)

        if successor:
            print(f"Successor of {val} -> {successor.val}")
        else:
            print(f"Successor of {val} -> None")