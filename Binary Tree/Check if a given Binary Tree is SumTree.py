class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
    if root is None:
        return 0
    return(sum(root.left) + root.data + sum(root.right))


def sumTree(root):
    if root is None or (root.left == None and root.right == None):
        return 1
    ls = sum(root.left)
    rs= sum(root.right)

    if((root.data == ls + rs) and sumTree(root.left) and sumTree(root.right)):
        return 1
    return 0  

if __name__ == "__main__":
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    if(sumTree(root)):
        print("SumTree ")
    else:
        print("not a SumTree ")

    