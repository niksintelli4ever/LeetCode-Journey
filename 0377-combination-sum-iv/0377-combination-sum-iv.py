class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(n,target):
            key=str(n)+"_"+str(target)
            if key in dp:
                return dp[key]
            if target==0:
                return 1
            if n>=len(nums) or target<0:
                return 0
            option=dfs(0,target-nums[n])+dfs(n+1,target)
            dp[key]=option
            return dp[key]
        
        return dfs(0,target)
        
            
        