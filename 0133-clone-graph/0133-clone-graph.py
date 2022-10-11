"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict1={}
        def dfs(root):
            if root in dict1:
                return dict1[root]
            copy=Node(root.val)
            dict1[root]=copy
            for neigh in root.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        return dfs(node) if node else None
    
        