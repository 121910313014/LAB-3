#TREE WITH 12 NODES RUN TIME INITIALISATION 
class Node:
    def __init__(self,data):
        self.left=None 
        self.right=None 
        self.data=data 
class BinaryTree:
    def __init__(self,root):
        self.root=root
    def insert_node(self,data,root):
        if root is None:
            root=Node(data)
        l=[root]
        while len(l)!=0:
            c=l.pop(0)
            if c.left is None:
                c.left=Node(data)
                break 
            l.append(c.left)
            if c.right is None:
                c.right=Node(data)
                break 
            l.append(c.right)
    def print_tree(self,root):
        if root:
            self.print_tree(root.left)
            print(root.data)  
            self.print_tree(root.right)
T=BinaryTree(Node(None))
n=int(input('Enter total number of elements to be inserted: '))
print('Enter Elements :')
for i in range(n):
    data=int(input())
    T.insert_node(data,T.root)
print('the structure of tree is : ')
T.print_tree(T.root)