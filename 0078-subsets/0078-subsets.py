class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,visit):
            if i==len(nums):
                res.append(visit.copy())
                return
            visit.append(nums[i])
            dfs(i+1,visit)
            visit.pop()
            dfs(i+1,visit)
        
        dfs(0,[])
        return res
        