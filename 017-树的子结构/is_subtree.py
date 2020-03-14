class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_subtree(pRoot1, pRoot2):
    if not pRoot1 or not pRoot2:
        return False
    return has_subtree(pRoot1, pRoot2) or \
           is_subtree(pRoot1.left, pRoot2) or \
           is_subtree(pRoot1.right, pRoot2)


def has_subtree(treeNode1, treeNode2):
    if not treeNode2:
        return True
    if not treeNode1:
        return False
    if treeNode1.val == treeNode2.val:
        return has_subtree(treeNode1.left, treeNode2.left) and \
               has_subtree(treeNode1.right, treeNode2.right)
    else:
        return False