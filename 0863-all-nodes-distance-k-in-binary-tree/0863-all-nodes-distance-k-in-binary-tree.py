# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g=defaultdict(list)   
        res=[]
        q=deque()
        visit=set()
        self.TtoG(root,None,g)
        q.append((target,0))
        while q:
            for i in range(len(q)):
                node,d=q.popleft()
                visit.add(node)
                if d==k:
                    res.append(node.val)

                for neigh in g[node]:
                    if neigh not in visit:
                        q.append((neigh,d+1))
        return res
    
    def TtoG(self,root,parent,g):
        if not root:
            return
        if parent:
            g[root].append(parent)
        if root.right:
            g[root].append(root.right)
            self.TtoG(root.right,root,g)
        if root.left:
            g[root].append(root.left)
            self.TtoG(root.left,root,g)
        
        