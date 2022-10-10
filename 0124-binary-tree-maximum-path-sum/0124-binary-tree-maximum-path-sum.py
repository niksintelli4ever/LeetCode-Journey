# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def maxSum(root):
            if not root:
                return 0
            leftmax=maxSum(root.left)
            rightmax=maxSum(root.right)
            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)
            res[0]=max(res[0],leftmax+rightmax+root.val)
        
            return max(leftmax+root.val,rightmax+root.val)
        maxSum(root)
        return res[0]
        