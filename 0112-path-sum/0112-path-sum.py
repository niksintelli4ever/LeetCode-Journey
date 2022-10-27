# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q=deque([[root,root.val]])
        while q:
            for i in range(len(q)):
                node,v=q.popleft()
                if not node.left and not node.right and v==targetSum:
                    return True
                if node.left:
                        q.append([node.left,node.left.val+v])
                if node.right:
                        q.append([node.right,v+node.right.val])
        
        return False
        
        