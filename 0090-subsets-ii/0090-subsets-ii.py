class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(i,visit):
            if i==len(nums):
                res.append(visit.copy())
                return
            visit.append(nums[i])
            dfs(i+1,visit)
            visit.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,visit)
        dfs(0,[])
        return res
        
        