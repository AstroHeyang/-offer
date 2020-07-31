def print(pRoot):
	if not pRoot:
	    return []
	queue = [pRoot]
	sign = 1
	res = []
	while queue:
	    cur_node, cur_vals = [], []
	    while queue:
	        cur_node.append(queue.pop(0))
	    for node in cur_node:
	        if node.left:
	            queue.append(node.left)
	        if node.right:
	            queue.append(node.right)
	        cur_vals.append(node.val)
	    if not sign % 2:
	        cur_vals = cur_vals[::-1]
	    sign += 1
	    res.append(cur_vals)
	return res
