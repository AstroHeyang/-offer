def get_next(pNode):
	if not pNode:
	    return None
	if pNode.right:
	    res = pNode.right
	    while res.left:
	        res = res.left
	    return res
	else:
	    while pNode.next:
	        if pNode.next.left == pNode:
	            return pNode.next
	        else:
	            pNode = pNode.next
	    if not pNode.next:
	        return
