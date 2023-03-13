class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def dfs(n):
            key=str(n)
            if key in dp:
                return dp[key]
            if n==0:
                return cost[0]
            if n==1:
                return cost[1]
            option=min(dfs(n-1)+cost[n],dfs(n-2)+cost[n])
            dp[key]=option
            return dp[key]
    
        return min(dfs(len(cost)-1),dfs(len(cost)-2))