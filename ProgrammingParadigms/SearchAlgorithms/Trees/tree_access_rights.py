# Given a tree of nodes design a way to know access rights of each node by looking up parent node information as well
class TreeNode:
    def __init__(self, name, parent=None, permissions=None):
        self.name = name
        self.parent = parent
        # Store permissions: e.g., {"read": True, "write": False}
        self.permissions = permissions if permissions is not None else {}
        self.children = []
        if parent:
            parent.children.append(self)
    
    def __repr__(self):
        return f"<Node: {self.name}>"

def get_effective_permission(node, perm_type) -> bool:
    """
    Finds the inherited or explicit permission for a node.
    Walks up the tree until a permission is found or the root is hit.
    """
    # Base Case 1: Current node defines the permission
    if perm_type in node.permissions:
        return node.permissions[perm_type]
    
    # Base Case 2: We hit the root and no permission was ever found
    if node.parent is None:
        return False # Default Deny policy

    # Recursive Step: Check the parent
    return get_effective_permission(node.parent, perm_type)

        
if __name__ == '__main__':
    # 1. Define a root with baseline permissions
    root = TreeNode("Global_Root", permissions={"read": True, "write": False})

    # 2. Subfolder inherits from root
    folder_a = TreeNode("Engineering_Folder", parent=root)

    # 3. File inherits 'read' from root, but overrides 'write' to be True
    file_b = TreeNode("Specs_File", parent=folder_a, permissions={"write": True})

    # Test the logic
    print(f"Read access for File_B: {get_effective_permission(file_b, 'read')}")     # True (from Root)
    print(f"Write access for File_B: {get_effective_permission(file_b, 'write')}")   # True (Override)
    print(f"Write access for Folder_A: {get_effective_permission(folder_a, 'write')}") # False (from Root)
