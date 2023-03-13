class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency={i:[] for i in range(numCourses)}
        for pre,crs in prerequisites:
            adjacency[pre].append(crs)
        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            if adjacency[crs]==[]:
                return True
            visit.add(crs)
            for neigh in adjacency[crs]:
                if not dfs(neigh):
                    return False
            visit.remove(crs)
            adjacency[crs]=[]
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
        