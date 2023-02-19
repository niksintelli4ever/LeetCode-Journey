# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
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
                if flag>0:
                    res.append(level)
                    flag=flag*-1
                else:
                    res.append(level[::-1])
                    flag=flag*-1
        
        return res
                    
                    
            
        