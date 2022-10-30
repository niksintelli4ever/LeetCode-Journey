# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,track,path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and track==node.val:
                res.append(path.copy())
            dfs(node.left,track-node.val,path)
            dfs(node.right,track-node.val,path)
            path.pop()
        dfs(root,targetSum,[])
        return res
        