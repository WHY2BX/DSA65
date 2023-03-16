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

    def delete(self, data):
        if self.is_empty():
            return "Cannot delete data."
        
        #หาตัวลบว่า
        parent = None
        node = self.root
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            else:
                node = node.right

        #กรณีหาโหนดไม่เจอ
        if not node:
            return BST.traverse
        
        # Case 1
        # Node no has children
        if not node.left and not node.right:
            if node == self.root:
                self.root = None
            elif node == parent.left:
                parent.left = None
            else:
                parent.right = None

        # Case 2-3
        # Node has children
        elif not node.left or not node.right:
            if node.left:
                child = node.left
            else:
                child = node.right
            if node == self.root:
                self.root = child
            elif node == parent.left:
                parent.left = child
            else:
                parent.right = child

        # Case 4     
        # Node has 2 subtrees
        else:
            delNodeParent = node
            delNode = node.left

            while delNode.right != None:
                delNodeParent = delNode
                delNode = delNode.right

            node.data = delNode.data

            if delNode == delNodeParent.left:
                delNodeParent.left = delNode.left
            else:
                delNodeParent.right = delNode.left
       
       


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
