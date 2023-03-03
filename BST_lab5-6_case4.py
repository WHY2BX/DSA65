class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root == None
    
    def insert(self, data):
        pNew = BSTNode(data)
        prev = None
        start = self.root
        if self.is_empty():
            self.root = pNew
        else:
            while start != None:
                if data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
            if data < prev.data:
                prev.left = pNew
            else:
                prev.right = pNew

    def preorder(self, root):
        if (root != None):
            print(' ->', root.data, end='')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print(' ->', root.data, end='')
            self.inorder(root.right)
            
    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(' ->', root.data, end='')
        
    def traverse(self):
        if self.is_empty():
            print("This is an empty tree!")
        else:
            print("\n[PreOrder] ")
            self.preorder(self.root)
            print("\n[InOrder]")
            self.inorder(self.root)
            print("\n[PostOrder]")
            self.postorder(self.root)
    
    def findMin(self):
        pointer = self.root
        while pointer.left != None:
            pointer = pointer.left
        return pointer.data

    def findMax(self):
        pointer = self.root
        while pointer.right != None:
            pointer = pointer.right
        return pointer.data

    def delete(self, node):
        prev = None
        start = self.root
        while start.data != node:
            if node < start.data:
                prev = start
                start = start.left
            else:
                prev = start
                start = start.right
        if self.root.data == node and start.left == None:
            self.root = start.right
        elif self.root.data == node and start.right == None:
            self.root = start.left
        #case1
        elif start.right == None and start.left == None:
            if prev.left == start:
                prev.left = None
            else:
                prev.right = None
        #case2-3
        elif start.right != None and start.left == None:
            if prev.left == start:
                prev.left = start.right
            else:
                prev.right = start.right
        elif start.right == None and start.left != None:
            if prev.left == start:
                prev.left = start.left
            else:
                prev.right = start.left
        #case4
        else:
            here = None
            thisis = start.left
            while thisis.right != None:
                here = thisis
                thisis = thisis.right
            if prev.left.data == start:
                prev.left = here.right
                here.right = None
            else:
                prev.right = here.right
                here.right = None
       


# myBST = BST()
# myBST.insert(14)
# myBST.insert(23)
# myBST.insert(7)
# myBST.insert(10)
# myBST.insert(33)
# myBST.insert(5)
# myBST.insert(20)
# myBST.insert(13)


# myBST.delete(5)
# myBST.traverse()
# print("\n----------")
# myBST.delete(33)
# myBST.traverse()

myBST2 = BST()
myBST2.insert(13)
myBST2.insert(7)
myBST2.insert(10)
myBST2.insert(23)
myBST2.insert(20)
print("\n----------")
myBST2.delete(7)
myBST2.traverse()

print("\n----------")
myBST2.delete(23)
myBST2.traverse()

# myBST.delete(14)
# myBST.traverse()