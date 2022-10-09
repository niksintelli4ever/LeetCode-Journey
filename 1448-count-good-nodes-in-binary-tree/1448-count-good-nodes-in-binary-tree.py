# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count=0
        res=0
        stack=[(root,root.val)]
        while stack:
            node,cmax=stack.pop()
            if node:
                res+=node.val>=cmax
                stack.append([node.left,max(cmax,node.val)])
                stack.append([node.right,max(cmax,node.val)])
        # print(maxval)
        return res
        