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
            print("[PreOrder] ")
            self.preorder(self.root)
            print("\n[InOrder]")
            self.inorder(self.root)
            print("\n[PostOrder]")
            self.postorder(self.root)
            
myBST = BST()
myBST.insert(10)
myBST.insert(20)
myBST.insert(25)
myBST.traverse()