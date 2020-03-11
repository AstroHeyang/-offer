class TreeNode:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None


def reConstructBinaryTree(pre, tin):
    if not pre or not tin:
        return
    root = TreeNode(pre[0])
    root_index = tin.index(pre[0])
    root.left = reConstructBinaryTree(pre[1:root_index+1], tin[:root_index])
    root.right = reConstructBinaryTree(pre[root_index+1:], tin[root_index+1:])
    return root
