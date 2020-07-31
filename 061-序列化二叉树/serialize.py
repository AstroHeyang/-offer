class Solution:
    def __init__(self):
        self.res = []
        
    def Serialize(self, root):
        # write code here
        if not root:
            return '#!'
        else:
            return (str(root.val) + '!' +
            self.Serialize(root.left) +
            self.Serialize(root.right))
    
    def Deserialize(self, s):
        string = s.split('!')
        return self.deserialize(string)
    
    def deserialize(self, string):
        # write code here
        var = string.pop(0)
        if var == '#':
            return None
        else:
            root = TreeNode(int(var))
            root.left = self.deserialize(string)
            root.right = self.deserialize(string)
        return root
