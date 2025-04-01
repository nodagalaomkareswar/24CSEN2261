class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# Example Usage
bst = BST()
root = None
elements = [20, 5, 1, 15, 9, 7, 12, 30, 25, 40, 45, 42]
for el in elements:
    root = bst.insert(root, el)

bst.inorder(root)
print("\n")

for el in [1, 40, 45, 9]:
    root = bst.delete(root, el)

bst.inorder(root)
print("\n")
