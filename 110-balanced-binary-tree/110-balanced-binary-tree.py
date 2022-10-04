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
        
        
        
    def depth(self,root):
        level=0
        if not root:
            return 0
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
            level+=1

        return level-1

        