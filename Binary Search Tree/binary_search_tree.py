class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        print("self.data in main", self.data)

    def insert(self, data):
        print("data is", data)
        print("self.data in insert is", self.data)
        if self.data:
            if data < self.data:
                print("less")
                if self.left is None:
                    self.left = Node(data)
                else:
                    print("Inserted in less")
                    self.left.insert(data)
            elif data > self.data:
                print("more")
                if self.right is None:
                    self.right = Node(data)
                else:
                    print("Inserted in more")
                    self.right.insert(data)
                    
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end = " ")
        self.inOrder(node.right)

    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)
    

if __name__ == "__main__":
    root = Node(10)
    # root.insert(12)
    root.insert(11)
    print("Insert 14")
    root.insert(7)
    root.insert(9)
    root.insert(15)
    root.insert(18)


    root.printTree()
   

    print("InOrder of tree is")
    root.inOrder(root)
    print("\n")
    print("PostOrder of  atree is")
    root.postOrder(root)
    print("\n")
    print("PreOrder of  a tree is")
    root.preOrder(root)

