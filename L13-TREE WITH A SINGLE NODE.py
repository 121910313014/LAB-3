#Binary Tree with a single node
class Node:
    def __init__(self,data):
        self.left=None 
        self.right=None 
        self.data=data    
class BinaryTree:
    def __init__(self,root):
        self.root=root 
    def print(self,root):
        print(root.data)
T=BinaryTree(Node(20))
T.print(T.root)