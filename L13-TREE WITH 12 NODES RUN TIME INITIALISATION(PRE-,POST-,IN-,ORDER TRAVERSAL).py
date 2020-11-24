#TYPES OF TREE TRAVERSALS
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
    def preorder(self,root):
        if root:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')  
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left) 
            self.postorder(root.right)
            print(root.data,end=' ') 
n=int(input('Enter total number of elements to be inserted: '))
print('Enter Elements :')
T=BinaryTree(Node(int(input())))
for i in range(n-1):
    data=int(input())
    T.insert_node(data,T.root)
print('\npre order of the tree is :')
T.preorder(T.root)
print('\nin order of the tree is :')
T.inorder(T.root)
print('\npost order of the tree is :')
T.postorder(T.root)