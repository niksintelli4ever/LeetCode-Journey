class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def rec(target,n):
            
            if target == 0 and n==len(nums):
                return 1
            
            if target!=0 and n==len(nums):
                return 0
            
            key = str(target) + '_' + str(n)
            
            if key in dp:
                return dp[key]
            
            dp[key] = rec(target+nums[n],n+1) + rec(target-nums[n],n+1)
            
            return dp[key]
        
        return rec(target, 0)
        