class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        @lru_cache
        def dfs(n,target):
            key=str(n)+"_"+str(target)
            if key in dp:
                return dp[key]
            if target==0:
                return 0
            if n>=len(coins) or target<0:
                return float("inf")
            option=min(1+dfs(n,target-coins[n]),dfs(n+1,target))
            dp[key]=option
            return dp[key]
        a=dfs(0,amount)
        return -1 if a==float("inf") else a
        