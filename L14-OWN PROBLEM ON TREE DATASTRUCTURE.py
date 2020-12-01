#Delete Even Leaves
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    def even_leaves(self,root):
        if root:
            root.left=self.even_leaves(root.left)
            root.right=self.even_leaves(root.right)
            if root.left is None and root.right is None and root.val%2==0:
                return None
            else :
                return root
        return None
    def print_tree(self,root):
        if root:
            self.print_tree(root.left)
            print(root.val,end=' ')  
            self.print_tree(root.right)
n=int(input('Enter total number of elements to be inserted: '))
print('Enter Elements :')
T=BinaryTree(Node(int(input())))
for i in range(n-1):
    val=int(input())
    T.insert_node(val,T.root)
print('Before deletion of even leaves :')
T.print_tree(T.root)
T.even_leaves(T.root)
print('\nAfter deletion of even leaves :')
T.print_tree(T.root)