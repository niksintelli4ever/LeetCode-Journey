class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(n,target):
            key=str(n)+"_"+str(target)
            if key in dp:
                return dp[key]
            if n==len(nums) and target==0:
                return 1
            if n>=len(nums) and target!=0:
                return 0
            option=0
            option+=dfs(n+1,target-nums[n])+dfs(n+1,target+nums[n])
        
            dp[key]=option
        
            return dp[key]
        
        return dfs(0,target)
        