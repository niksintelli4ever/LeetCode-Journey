# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g=defaultdict(list)
        self.tTog(root,None,g)
        q=deque([[target,0]])
        visit=set()
        res=[]
        while q:
            for i in range(len(q)):
                node,d=q.popleft()
                if d==k:
                    res.append(node.val)
                visit.add(node)
                for neigh in g[node]:
                    if neigh not in visit:
                        q.append([neigh,d+1])
        
        return res
        
                
    
    
    
    
    
    
    
    
    
    def tTog(self,root,parent,g):
        if not root:
            return
        if parent:
            g[root].append(parent)
        if root.left:
            g[root].append(root.left)
            self.tTog(root.left,root,g)
        if root.right:
            g[root].append(root.right)
            self.tTog(root.right,root,g)
        