class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i,sum1,visit):
            if sum1==target:
                res.append(visit.copy())
                return
            if i>=len(candidates) or sum1>target:
                return
            visit.append(candidates[i])
            dfs(i+1,sum1+candidates[i],visit)
            visit.remove(candidates[i])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum1,visit)
        
        dfs(0,0,[])
        return res