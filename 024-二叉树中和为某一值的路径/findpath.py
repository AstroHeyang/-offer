class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def find_path(self, root, num: int):
        if not root:
            return
        self.path.append(root.val)
        num -= root.val
        if num == 0 and not root.left and not root.right:
            self.res.append(self.path[:])
        if root.left:
            self.find_path(root.left, num)
        if root.right:
            self.find_path(root.right, num)
        self.path.pop()
        return self.res