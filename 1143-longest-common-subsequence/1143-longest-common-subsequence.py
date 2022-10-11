class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        
        return dp[m-1][n-1]
            
        