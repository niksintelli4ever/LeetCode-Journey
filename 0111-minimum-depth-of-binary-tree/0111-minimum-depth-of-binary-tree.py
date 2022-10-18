# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        level=1
        minlevel=float(inf)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node and not node.right and not node.left:
                    minlevel=min(level,minlevel)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        
        return minlevel
        