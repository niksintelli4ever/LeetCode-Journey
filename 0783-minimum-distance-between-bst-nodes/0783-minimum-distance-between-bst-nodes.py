# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        print(res)
        maxres=float("inf")
        for i in range(1,len(res)):
            maxres=min(maxres,res[i]-res[i-1])
        
        return maxres
            
        
        
        
                
        