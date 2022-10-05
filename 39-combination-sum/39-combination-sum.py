class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def recursiveFunction(i,visit,sum1):
            if i>=len(candidates) or sum1>target:
                return
            if sum1==target:
                res.append(visit.copy())
                return
            visit.append(candidates[i])
            recursiveFunction(i,visit,sum1+candidates[i])
            visit.remove(candidates[i])
            recursiveFunction(i+1,visit,sum1)
        
        recursiveFunction(0,[],0)
        return res
        