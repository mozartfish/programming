class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# root of tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
