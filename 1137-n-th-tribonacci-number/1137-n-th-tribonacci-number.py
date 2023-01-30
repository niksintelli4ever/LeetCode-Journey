class Solution:
    def tribonacci(self, n: int) -> int:
        dp={}
        def tribo(n):
            key=str(n)
            if key in dp:
                return dp[key]
            if n==0:
                dp[key]=0
            elif n==1:
                dp[key]=1
            elif n==2:
                dp[key]=1
            else:
                dp[key]=tribo(n-1)+tribo(n-2)+tribo(n-3)
            return dp[key]
        a=tribo(n)
        return a
                
            
        