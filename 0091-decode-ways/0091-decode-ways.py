class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def dfs(n):
            key=str(n)
            if key in dp:
                return dp[key]
            if n>=len(s):
                return 1
            if s[n]=='0':
                return 0
            option=dfs(n+1)
            if (n+1<len(s) and (s[n]=='1' or s[n]=='2' and s[n+1] in "0123456")):
                option+=dfs(n+2)
            dp[key]=option
            return dp[key]
        return dfs(0)
        
        