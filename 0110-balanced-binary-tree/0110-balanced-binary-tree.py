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
        if abs(self.depth(root.left)-abs(self.depth(root.right)))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    
    
    
    def depth(self,root):
        maxdepth=0
        if not root:
            return 0
        stack=[[root,1]]
        while stack:
            node,d=stack.pop()
            if node:
                maxdepth=max(maxdepth,d)
                stack.append([node.left,d+1])
                stack.append([node.right,d+1])
        
        return maxdepth
                
            
        
        