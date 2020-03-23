class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None


def convert(pRootOfTree):
    if not pRootOfTree:
        return pRootOfTree
    if not pRootOfTree.left and not pRootOfTree.right:
        return pRootOfTree

    # 处理左子树
    convert(pRootOfTree.left)
    # 连接根与左子树最大结点
    left = pRootOfTree.left
    if left:
        while left.right:
            left = left.right
        pRootOfTree.left, left.right = left, pRootOfTree

    # 处理右子树
    convert(pRootOfTree.right)
    # 连接根与右子树最小结点
    right = pRootOfTree.right
    if right:
        while right.left:
            right = right.left
        pRootOfTree.right, right.left = right, pRootOfTree

    while pRootOfTree.left:
        pRootOfTree = pRootOfTree.left
    return pRootOfTree
