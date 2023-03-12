# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0
        q=deque([[root,root.val]])
        while q:
            for i in range(len(q)):
                node,d=q.popleft()
                if node and not node.left and not node.right and d==targetSum:
                    return True
                if node.left:
                    q.append([node.left,d+node.left.val])
                if node.right:
                    q.append([node.right,d+node.right.val])
            
        return False
        