def print(pRoot):
	if not pRoot:
	    return []
	queue = [pRoot]
	res = []
	while queue:
	    this_array, cur_node = [],[]
	    while queue:
	        cur_node.append(queue.pop(0))
	        
	    for node in cur_node:
	        this_array.append(node.val)
	        if node.left:
	            queue.append(node.left)
	        if node.right:
	            queue.append(node.right)
	    
	    res.append(this_array)
	return res
