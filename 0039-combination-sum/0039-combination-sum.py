class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,visit,t):
            if t==target:
                res.append(visit.copy())
                return
            if i>=len(candidates) or t>target:
                return
            visit.append(candidates[i])
            dfs(i,visit,t+candidates[i])
            visit.pop()
            dfs(i+1,visit,t)
        
        dfs(0,[],0)
        return res