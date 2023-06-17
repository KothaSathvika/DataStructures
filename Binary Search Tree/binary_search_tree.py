#### BASIC APPROACH TO FIND LEVEL ORDER #### TIME COMPLEXITY O(n^2)
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
        
def printCurrentLevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.data, end = " ")
        return
    elif level > 1:
        printCurrentLevel(node.left, level-1)
        printCurrentLevel(node.right, level-1)

def levelOrder(node):
    h = height(node)
    for i in range(1, h+1):
        printCurrentLevel(node, i)

### BFS implementation using Queues #### O(n)
def levelOrderQueue(node):
    # print(node.left)
    if node is None:
        return
    queue = []
    queue.append(node)
    while (len(queue) > 0):
        print(queue[0].data, end = " ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)



class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        # print("self.data in main", self.data)

    def insert(self, data):
        # print("data is", data)
        # print("self.data in insert is", self.data)
        if self.data:
            if data < self.data:
                # print("less")
                if self.left is None:
                    self.left = Node(data)
                # else:
                #     print("Inserted in less")
                    self.left.insert(data)
            elif data > self.data:
                # print("more")
                if self.right is None:
                    self.right = Node(data)
                else:
                    # print("Inserted in more")
                    self.right.insert(data)
                    
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    ### INORDER TRAVERSAL - TIME COMPLEXITY O(n) ###
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end = " ")
        self.inOrder(node.right)

    ### PREORDER TRAVERSAL - TIME COMPLEXITY O(n) ###
    def preOrder(self, node):
        if node is None:
            return
        print(node.data, end = " ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    ### POSTORDER TRAVERSAL - TIME COMPLEXITY O(n) ###
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end = " ")
    

        

if __name__ == "__main__":
    root = Node(10)
    # root.insert(12)
    root.insert(11)
    # print("Insert 14")
    root.insert(7)
    root.insert(9)
    root.insert(15)
    root.insert(18)


    # root.printTree()
   

    print("InOrder of tree is")
    root.inOrder(root)
    print("\n")
    print("PostOrder of  atree is")
    root.postOrder(root)
    print("\n")
    print("PreOrder of  a tree is")
    root.preOrder(root)
    print("\n")
    print("levelOrder of  atree is")
    levelOrder(root)
    print("\n")

    levelOrderQueue(root)

