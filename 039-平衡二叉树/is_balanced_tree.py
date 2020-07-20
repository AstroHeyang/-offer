def is_balanced_tree(pRoot):

	def height_of_tree(node):
		if not node:
			return 0
		height_left = height_of_tree(node.left)
		height_right = height_of_tree(node.right)
		if height_left == -1:
			return -1
		if height_right == -1:
			return -1
		if abs(height_left - height_right) > 1:
			return -1
		else:
			return 1 + max(height_left, height_right)
	return height_of_tree(pRoot) != -1 

