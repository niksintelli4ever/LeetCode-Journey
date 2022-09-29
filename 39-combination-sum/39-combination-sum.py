class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        res=[]
        def combo(i,subset,sum1):
            if sum1==target:
                res.append(subset.copy())
                return
            if i>=len(candidates):
                return
            if sum1>target:
                return
            subset.append(candidates[i])
            combo(i,subset,sum1+candidates[i])
            subset.remove(candidates[i])
            combo(i+1,subset,sum1)
        
        combo(0,[],0)
        return res
        