class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_from_top_to_bottom(root):
    if not root:
        return
    if not root.left and root.right:
        return root.val
    dqueue = [root]
    res = []
    while dqueue:
        tree_node = dqueue[0]
        res.append(tree_node.val)
        if tree_node.left:
            dqueue.append(tree_node.left)
        if tree_node.right:
            dqueue.append(tree_node.right)
        dqueue.pop(0)
    return res
