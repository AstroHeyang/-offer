def tree_depth(pRoot):
	if not pRoot:
        return 0
    return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1 
