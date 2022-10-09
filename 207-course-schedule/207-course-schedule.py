class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency={i:[] for i in range(numCourses)}
        visit=set()
        for crs,pre in prerequisites:
            adjacency[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if adjacency[crs]==[]:
                return True
            visit.add(crs)
            for pre in adjacency[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adjacency[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
                
                