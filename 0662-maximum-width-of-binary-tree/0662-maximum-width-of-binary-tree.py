# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([[root,1]])
        maxwidth=1
        while q:
            for i in range(len(q)):
                node,d=q.popleft()
                if node.left:
                    q.append([node.left,d*2])
                if node.right:
                    q.append([node.right,d*2 +1])
            if q:
                width=q[-1][1]-q[0][1]+1
                maxwidth=max(width,maxwidth)
        
        return maxwidth
        