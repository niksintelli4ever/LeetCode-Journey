# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        q=deque([[root,root.val,[root.val]]])
        res=[]
        while q:
            for i in range(len(q)):
                node,d,path=q.popleft()
                if node and not node.left and not node.right and d==targetSum:
                    res.append(path)
                if node.left:
                    q.append([node.left,d+node.left.val,path+[node.left.val]])
                if node.right:
                    q.append([node.right,d+node.right.val,path+[node.right.val]])
        return res
        