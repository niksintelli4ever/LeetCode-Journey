# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g=defaultdict(list)
        visit=set()
        q=deque()
        res=[]
        self.convertTreetoG(root,None,g)
        q.append((target,0))
        while q:
            for i in range(len(q)):
                n,d=q.popleft()
                visit.add(n)
                if d==k:
                    res.append(n.val)
                
                for neigh in g[n]:
                    if neigh not in visit:
                        q.append((neigh,d+1))
        
        return res
        
        
        
    def convertTreetoG(self,node,parent,g):
            if not node:
                return
            if parent:
                g[node].append(parent)
            if node.right:
                g[node].append(node.right)
                self.convertTreetoG(node.right,node,g)
            if node.left:
                g[node].append(node.left)
                self.convertTreetoG(node.left,node,g)
    
        