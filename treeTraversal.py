class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end="")
        inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(8)
root.right.left = Node(30)
root.right.right = Node(67)
root.right.left.right = Node(56)


print("inorder traversal")
inorder(root)