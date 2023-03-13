class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp={}
        def dfs(n,target):
            key=str(n)+"_"+str(target)
            if key in dp:
                return dp[key]
            if target==0:
                return True
            if n>=len(nums) or target<0:
                return False
            option1=dfs(n+1,target-nums[n])
            option2=dfs(n+1,target)
            dp[key]=option1 or option2
            return dp[key]
        return dfs(0,target)

            
        