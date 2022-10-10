# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack=[[root,root.val]]
        res=0
        while stack:
            node,valu=stack.pop()
            if node:
                res+=node.val>=valu
                stack.append([node.left,max(valu,node.val)])
                stack.append([node.right,max(valu,node.val)])
        
        return res
                
        
        