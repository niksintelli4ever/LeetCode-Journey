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
        stack=[[root,root.val]]
        while stack:
               node,nodeval=stack.pop()
               if not node.left and not node.right and nodeval==targetSum:
                        return True
               if node.left:
                    stack.append([node.left,node.left.val+nodeval])
               if node.right:
                    stack.append([node.right,nodeval+node.right.val])
        
        return False