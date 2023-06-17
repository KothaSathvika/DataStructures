class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSibling(root, node1, node2):
    if root is None:
        return 0
    
    return ((root.left == node1 and root.right ==node2) or
            (root.left == node2 and root.right == node1)or
            isSibling(root.left, node1, node2) or
            isSibling(root.right, node1, node2))

def treeLevel(root, node, level):
    if root is None:
        return 0
    if root == node:
        return level
    
    l = treeLevel(root.left, node, level+1)
    print("l is", l)
    if l!=0:
        return l
    
    return treeLevel(root.right, node, level+1)    

def isCousin(root, node1, node2):
    if ((treeLevel(root, node1, 1) == treeLevel(root, node2, 1)) and not (isSibling(root, node1, node2))):
        return 1
    return 0

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    node1 = root.left.right
    node2 = root.right.right

    if isCousin(root, node1, node2) == 1:
        print("yes")
    else:
        print("No")