class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        
        def climb(n):
            # print(n)
            key=str(n)
            if key in dp:
                return dp[key]
            if n==0:
                return 1
            elif n==1:
                return 1
            else:
                dp[key]=climb(n-1)+climb(n-2)
            return dp[key]
        a=climb(n)
        return a