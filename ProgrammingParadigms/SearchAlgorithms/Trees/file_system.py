# Design a File System

# Step 0: Clarify the requirements
#   1. Basic operations:
#       - Create file/folder
#       - Read file
#       - Write file
#       - Delete file/folder
#       - List folder contents
#   2. Constraints:
#       - Single user or multi-user? → start with single
#       - In-memory or persistent? → start in-memory
#       - Permissions required? → optional
#   3. Scale:
#       - Number of files/folders? Start small for simplicity
#       - Maximum path length? Assume reasonable limits
# Step 2 — Define Core Operations

class FileNode:
    def __init__(self, name, is_file=False, content="", parent=None):
        self.name = name
        self.is_file = is_file
        self.content = content  # Only for files
        self.parent = parent    # Fixed: setting the parent properly
        self.children = {}      # dict: name -> FileNode
        if parent:
            parent.children[name] = self
    
    def create(self, name, is_file=False):
        if self.is_file:
            raise ValueError("Cannot create inside a file")
        if name in self.children:
            raise ValueError(f"Name '{name}' already exists")
        
        # Returns new node and automatically links via __init__
        return FileNode(name, is_file=is_file, parent=self)
    
    def write_file(self, data):
        if not self.is_file:
            raise ValueError("Not a file")
        self.content = data

    def read_file(self):
        if not self.is_file:
            return ValueError("Not a file")
        return self.content
    
    def list_folder(self):
        if self.is_file:
            raise ValueError("Not a folder")
        return list(self.children.keys())
    
    def delete(self):
        if self.parent:
            self.parent.children.pop(self.name, None)
        self.parent = None

    @staticmethod
    def traverse_path(root, path):
        if not path or path == "/":
            return root
        parts = path.strip("/").split("/")
        current = root
        for part in parts:
            if part not in current.children:
                raise ValueError(f"Path not found: {part}")
            current = current.children[part]
        return current

if __name__ == "__main__":
    # Initialize Root
    root = FileNode("root", is_file=False)

    # 1. Create folders
    folder_a = root.create("FolderA")
    folder_b = root.create("FolderB")

    # 2. Create and write to file
    file1 = folder_a.create("File1.txt", is_file=True)
    file1.write_file("Hello FDSE!")

    # 3. List folder contents
    print(f"Root contents: {root.list_folder()}")        # ['FolderA', 'FolderB']
    print(f"FolderA contents: {folder_a.list_folder()}") # ['File1.txt']

    # 4. Read file
    print(f"File1 content: {file1.read_file()}")         # "Hello FDSE!"

    # 5. Path Traversal Test
    found_node = FileNode.traverse_path(root, "/FolderA/File1.txt")
    print(f"Found via path: {found_node.name}")
