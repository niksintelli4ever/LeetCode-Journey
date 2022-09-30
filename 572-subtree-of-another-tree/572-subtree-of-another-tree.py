# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isSameTree(self,l1,l2):
        if not l1 and not l2:
            return True
        if not l1 or not l2:
            return False
        if l1.val!=l2.val:
            return False
        
        return self.isSameTree(l1.left,l2.left) and self.isSameTree(l1.right,l2.right)        
        