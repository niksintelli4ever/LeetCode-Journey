# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level=[]
        arr=[]
        count=0
        sum1=0
        stack=[[root,[root.val]]]
        while stack:
            node,path=stack.pop()
            if node and not node.left and not node.right:
                level.append(path)
            if node.left:
                stack.append([node.left,path+[node.left.val]])
            if node.right:
                stack.append([node.right,path+[node.right.val]])
        for i in level:
            arr=[]
            for j in i:
                arr.append(j)
            x=0
            while arr:
                x+=arr.pop(0)
                x=x*10
            sum1+=x
        return sum1//10
        print(count)
                
        
                       
                
        
        