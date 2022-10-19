class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        n=len(nums)
        def rec(target,n):
            
            if target == 0 and n==0:
                return 1
            
            if target!=0 and n==0:
                return 0
            
            key = str(target) + '_' + str(n)
            
            if key in dp:
                return dp[key]
            
            dp[key] = rec(target+nums[n-1],n-1) + rec(target-nums[n-1],n-1)
            
            return dp[key]
        
        return rec(target,n )
        