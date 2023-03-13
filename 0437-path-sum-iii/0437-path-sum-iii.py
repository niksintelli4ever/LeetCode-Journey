# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        q=deque([[root,[root.val]]])
        count=0
        while q:
            for i in range(len(q)):
                node,s1=q.popleft()
                count+=s1.count(targetSum)
                if node.left:
                    q.append([node.left,[x+node.left.val for x in s1]+[node.left.val]])
                if node.right:
                    q.append([node.right,[x+node.right.val for x in s1]+[node.right.val]])
        return count
        