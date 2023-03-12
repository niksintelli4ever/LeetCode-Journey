class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(n,buying):
            if n>=len(prices):
                return 0
            key=str(n)+"_"+str(buying)
            if key in dp:
                return dp[key]
            if buying:
                buy=dfs(n+1,not buying)-prices[n]
                cooldown=dfs(n+1,buying)
                option=max(buy,cooldown)
                dp[key]=option
            
            if not buying:
                sell=dfs(n+2,not buying)+prices[n]
                cooldown=dfs(n+1,buying)
                option=max(sell,cooldown)
                dp[key]=option
            
            return dp[key]
        
        return dfs(0,True)
            
        