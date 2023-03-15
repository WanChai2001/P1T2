class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data == self.data :
                print("Duplicade Data")
        else:
            self.data = data

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print("->" + str(self.data) , end=''),
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print("->" + str(self.data) , end=''),
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print("->" + str(self.data) , end=''),


print("\n[ Tree Current ]\n")
n = int(input("Enter amount of tree node : "))
dataRoot = int(input("Enter root node data : "))
root = Node(dataRoot)
for i in range (n-1) :
    dataChild= int(input("Enter child node data : "))
    root.insert(dataChild)

print("\n[ Tree Traversing. . . ]")
print("\n[ Inorder Traversal :")
root.inorder_traversal()
print("\n")
print("\n[ Preorder Traversal :")
root.preorder_traversal()
print("\n")
print("\n[ Postorder Traversal :")
root.postorder_traversal()
print("\n")
            
