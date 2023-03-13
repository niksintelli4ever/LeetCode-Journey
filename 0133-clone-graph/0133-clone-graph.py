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
        def dfs(node):
            if node in dict1:
                return dict1[node]
            copy=Node(node.val)
            dict1[node]=copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
        
            return copy
        return None if not node else dfs(node)
        