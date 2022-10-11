class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        adjacency={i:[] for i in range(numCourses)}
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
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
                
        