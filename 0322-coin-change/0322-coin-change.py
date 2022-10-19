class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        a=0
        n=len(coins)
        
        if amount == 0:
            return 0
        
        dp={}
        
        def coinC(n,amount):
            
            # print(n,amount, count)
            key=str(n) + '_' + str(amount)
            # print(key)
            if key in dp:
                # print("Key in MEMO", dp[key])
                return dp[key]
            
            if amount == 0:
                return 0
            
            if n<=0:
                return float('inf')
            
            # min_so_far = float('inf')
            if coins[n-1]<=amount:
                # print("IF")
                dp[key]= min( 1 + coinC(n,amount-coins[n-1]) , coinC(n-1,amount))
            
            else:
                # print("ELSE")
                dp[key] = coinC(n-1,amount)
            
            # dp[key] = min_so_far
            
            return dp[key]
        
        
        a=coinC(n,amount)
        # print(dp)   

        return -1 if a == float('inf') else a
            
            
                
            
        