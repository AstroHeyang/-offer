class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.res = []
        
    def InOrderTraversal(self, pRoot):
        if not pRoot:
            return pRoot
        self.InOrderTraversal(pRoot.left)
        self.res.append(pRoot)
        self.InOrderTraversal(pRoot.right)
        return self.res
        
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0 or not pRoot:
            return 
        inOrder = self.InOrderTraversal(pRoot)
        if k > len(inOrder):
            return 
        return inOrder[k-1]
