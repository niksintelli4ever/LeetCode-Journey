class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,visit):
            if len(visit)==len(nums):
                res.append(visit.copy())
                return
            if i>=len(nums):
                return
            for j in range(0,len(nums)):
                if nums[j] not in visit:
                    visit.append(nums[j])
                    dfs(i+1,visit)
                    visit.pop()
            
        dfs(0,[])
        return res
        