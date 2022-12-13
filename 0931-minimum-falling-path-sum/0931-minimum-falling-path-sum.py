class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix)
        dp=[[0 for i in range(m)] for j in range(n)]
        dp[0]=matrix[0]
        for r in range(1,n):
            for c in range(n):
                if c>0 and c<n-1:
                    dp[r][c]=matrix[r][c]+min(dp[r-1][c],dp[r-1][c-1],dp[r-1][c+1])
                if c==0:
                    dp[r][c]=matrix[r][c]+min(dp[r-1][c],dp[r-1][c+1])
                if c==n-1:
                    dp[r][c]=matrix[r][c]+min(dp[r-1][c],dp[r-1][c-1])
        return min(dp[-1])
            