class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        maxarea=0
        a=0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                return 0
            grid[r][c]="#"
            return 1+dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    a=max(a,dfs(r,c))
        return a
                
        