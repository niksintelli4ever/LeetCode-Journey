class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=cols or grid[r][c]!='1':
                return
            grid[r][c]='#'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
    
        for r in range(row):
            for c in range(cols):
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c)
                    
        
        return count
        