class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def coinC(n,amount):
            key=str(n)+"_"+str(amount)
            if key in dp:
                return dp[key]
            if amount==0:
                return 0
            if n>=len(coins) or amount<0:
                return float("inf")
            option1=min(1+coinC(n,amount-coins[n]),coinC(n+1,amount))
            
            dp[key]=option1
        
            return dp[key]
        a=coinC(0,amount)   
        return -1 if a==float("inf") else a
    
        