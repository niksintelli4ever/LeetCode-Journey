# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.depth(root.left)-self.depth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
         
    def depth(self,node):
        maxdepth=0
        if not node:
            return 0
        stack=[[node,1]]
        while stack:
            n,depth=stack.pop()
            if n:
                maxdepth=max(maxdepth,depth)
                stack.append([n.left,depth+1])
                stack.append([n.right,depth+1])
        
        return maxdepth
            
        