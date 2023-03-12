class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        def dfs(n,target):
            key=str(n)+"_"+str(target)
            if key in dp:
                return dp[key]
            if target==0:
                return True
            if n>=len(nums) or target<0:
                return False
            option=dfs(n+1,target-nums[n]) or dfs(n+1,target)
            dp[key]=option
            return dp[key]
        
        return dfs(0,target)
        