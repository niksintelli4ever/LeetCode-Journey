class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def fib(n):
            key=str(n)
            if key in dp:
                return dp[key]
            if n==0:
                return 1
            if n==1:
                return 1
            dp[key]=fib(n-1)+fib(n-2)
            return dp[key]
    
        return fib(n)
            
            
        