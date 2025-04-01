class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)
    
    def preorder_traversal(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    
    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=' ')
    
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        return root

# Example usage
tree = BinaryTree()
root = None
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    root = tree.insert(root, value)

print("Inorder Traversal:")
tree.inorder_traversal(root)
print("\nPreorder Traversal:")
tree.preorder_traversal(root)
print("\nPostorder Traversal:")
tree.postorder_traversal(root)

print("\nDeleting 20")
root = tree.delete_node(root, 20)
print("Inorder Traversal after deletion:")
tree.inorder_traversal(root)
