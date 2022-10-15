# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return None
            root=TreeNode(max(nums))
            index=nums.index(root.val)
            root.left=dfs(nums[:index])
            root.right=dfs(nums[index+1:])
            return root
                          
        return dfs(nums)
    
            
        
        