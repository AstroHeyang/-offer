def isSymmetrical(pRoot):
	if not pRoot:
	    return True 
	return self.isEqualNode(pRoot.left, pRoot.right)
    
def isEqualNode(leftNode, rightNode):
    if not leftNode and not rightNode:
        return True
    elif not leftNode or not rightNode:
        return False
    if leftNode.val == rightNode.val:
        return (self.isEqualNode(leftNode.left, rightNode.right) 
                and self.isEqualNode(leftNode.right, rightNode.left))
    else:
        return False
