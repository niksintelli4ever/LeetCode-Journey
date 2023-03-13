class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,visit,t):
            if t==target:
                res.append(visit.copy())
                return
            if i>=len(candidates) or t>target:
                return
            visit.append(candidates[i])
            dfs(i+1,visit,t+candidates[i])
            visit.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,visit,t)
        
        dfs(0,[],0)
        return res
        