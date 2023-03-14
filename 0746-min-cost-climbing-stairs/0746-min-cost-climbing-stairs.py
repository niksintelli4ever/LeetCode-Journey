class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        n=len(cost)
        def dfs(n):
            key=str(n)
            if key in dp:
                return dp[key]
            if n==0:
                return cost[0]
            if n==1:
                return cost[1]
            option=dfs(n-1)+cost[n]
            option2=dfs(n-2)+cost[n]
            dp[key]=min(option,option2)
            return dp[key]
        
        return min(dfs(n-1),dfs(n-2))
            
        