class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def dfs(n,amount):
            key=str(n)+"_"+str(amount)
            if key in dp:
                return dp[key]
            if n>=len(coins) or amount<0:
                return 0
            if amount==0:
                return 1
            option = dfs(n,amount-coins[n])+dfs(n+1,amount)
            dp[key]=option
            return dp[key]
        return dfs(0,amount)
        