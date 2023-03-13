class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        cycle=set()
        res=[]
        adjacency={i:[] for i in range(numCourses)}
        for pre,crs in prerequisites:
            adjacency[pre].append(crs)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            visit.add(crs)
            cycle.add(crs)
            for nei in adjacency[crs]:
                if not dfs(nei):
                    return False
            
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        
        return res