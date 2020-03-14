class TreeNode:
    def __init__(self, val):
        self.val = val

def mirror(pRoot):
    if not pRoot:
        return pRoot
    if not pRoot.left and not pRoot.right:
        return pRoot
    pRoot.left, pRoot.right = pRoot.right, pRoot.left
    mirror(pRoot.left)
    mirror(pRoot.right)
        self.left = None
        self.right = None
