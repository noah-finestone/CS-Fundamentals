# Binary Search Tree
# Height differnce between any two nodes must be <= 0
# 
# BST rule: smaller goes left, larger goes right.

class Node:
    def __init__(self, value: int, left=None, right=None, height=0):
        self.value = value   # (1) Int value
        self.left = left     # (2) Left child node
        self.right = right   # (3) Right child node
        self.height = height

class BinarySearchTree:
    def __init__(self, root_value: int = None):
        self.root_value = Node(root_value) if root_value is not None else None
    
    def getValue(self):
        return self.root_value.value if self.root_value else None
    
    def height(self, node):
        if node == None:
            return -1
        return node.height
    
    def isEmpty(self):
        return self.root_value is None
    
    def display(self):
        return self._display(self.root_value, "Root Node: ")
    
    def _display(self, node: Node, details: str):
        if node is None:
            return
        print(details + str(node.value))
        self._display(node.left, "Left of " + str(node.value) + ": ")
        self._display(node.right, "Right of " + str(node.value) + ": ")

    def insert(self, value: int):
        self.root_value = self._insert(self.root_value, value)
    
    def _insert(self, node: Node, value: int) -> Node: 
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return node
    
    def balanced(self):
        return self._balanced(self.root_value)
    
    def _balanced(self, node):
        if node is None:
            return True
        return abs(self.height(node.left) - self.height(node.right)) <= 1 and self._balanced(node.left) and self._balanced(node.right)
    

    def populateSorted(self, arr):
        self.root_value = self._populateSorted(arr, 0, len(arr) - 1)

    def _populateSorted(self, arr, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        node = Node(arr[mid])

        node.left = self._populateSorted(arr, start, mid - 1)
        node.right = self._populateSorted(arr, mid + 1, end)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        return node

if __name__ == "__main__":
    # bst = BinarySearchTree()
    # balancedBST = BinarySearchTree()

    # values = [10, 5, 15, 3, 7, 12, 18]
    # sorted_values = [1,2,3,4,5,6,7,8,9,10]

    # for v in values:
    #     bst.insert(v)
    # for v in sorted_values:
    #     balancedBST.insert(v)

    #     print("Root:", bst.root_value.value)   
    # print("Is balanced:", bst.balanced())  
    # print("--- Printing Tree ---")
    # bst.display()
    # print("Unbalanced Tree with sorted valued:")
    # print("Root: ", balancedBST.root_value.value)
    # balancedBST.balanced()
    # balancedBST.display()
    bst = BinarySearchTree()

    # Sorted array
    arr = [3, 5, 7, 10, 12, 15, 18]

    # Build BST from sorted array
    bst.populateSorted(arr)

    # Display tree
    bst.display()

    # Check if balanced
    print("Is balanced:", bst.balanced())

#         10
#       /    \
#      5      15
#     / \    /  \
#    3   7  12  18


 