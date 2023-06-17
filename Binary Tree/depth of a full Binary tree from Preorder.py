def findDepthRec(tree, n, index):
    if (index[0] >= n or tree[index[0]] == 'l'):
        return 0
    index[0] += 1
    left = findDepthRec(tree, n, index)

    index[0] += 1
    right = findDepthRec(tree, n, index)

    return (max(left,right)+1)


def findDepth(tree, n):

    index = [0]
    return findDepthRec(tree, n, index)

if __name__ == "__main__":
    tree = "nlnnlll"
    n = len(tree)

    print(findDepth(tree, n))

