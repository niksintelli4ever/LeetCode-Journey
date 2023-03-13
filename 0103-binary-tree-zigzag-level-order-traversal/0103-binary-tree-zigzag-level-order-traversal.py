# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        res=[]
        flag=1
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                if flag:
                    res.append(level)
                    flag=0
                else:
                    res.append(level[::-1])
                    flag=1
        return res
                
        