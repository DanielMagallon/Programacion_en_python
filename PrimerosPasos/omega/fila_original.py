class Node:
    def __init__(self,data):
        self.left: Node = None
        self.right: Node = None
        self.data = data

    def add_left(self,left):
        self.left = left

    def add_right(self,rigt):
        self.right = rigt

class BinaryTree:

    def __init__(self):
        self.root:Node = None

    def insert_data(self,data):
        if self.root: ...

        else:
            self.root = Node(data)
