class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

## get level using recursive function### O(n), if it's not a balanced binary tree and O(logn) if it is a binary tree
def getLevel(root, key, level):
    if root is None:
        # print("root is None")
        return 0

    if root.data == key:
        # print("data is key and level is ", level)
        return level
    # print("root.data is", root.data, "level is", level)
    # print("***********************************")
    
    # print("on left side of ", root.data)
    l=getLevel(root.left, key, level +1)
    # print("at left of " + str(root.data) + " l is " ,l)
    if l != 0:
        # print(l)
        return l
    # print("on right side of", root.data)
    return(getLevel(root.right, key, level+1))

### Get level using queue #### TimeComplexity: O(n)

def getLevelQueue(root, key):
    if root is None:
        return 0
    q = []
    q.append(root)
    level = 0
    while(len(q) > 0):
        n = len(q)
        for i in range(n):
            node = q.pop(0)

            if node.data == key:
                return level
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        level += 1

    return 0

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(6)
    root.right.right.right = Node(8)
    root.right.right.left = Node(9)

    # print(getLevel(root, 9, 0))
    print(getLevelQueue(root, 8))