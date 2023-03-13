class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        m=len(text1)
        n=len(text2)
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[m-1][n-1]        