
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =None

def constructATree(level, inorder):
    if inorder:
        # inorderrder_index = -1
        for i in range(0, len(level)):
            if level[i] in inorder:
                # print(level[i])
                node = Node(level[i])
                inorder_index = inorder.index(level[i])
                break
        node.left = constructATree(level, inorder[0:inorder_index])
        node.right = constructATree(level, inorder[inorder_index+1:len(inorder)])
        return node
    else:
        return None

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)

if __name__ == "__main__":
    inorder    = [4, 8, 10, 12, 14, 20, 22]
    level = [20, 8, 22, 4, 12, 10, 14]
    root = constructATree(level, inorder)

    inOrder(root)