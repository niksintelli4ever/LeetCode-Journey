class Solution(object):
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j]:
                return True
            visited[i][j] = True
            if grid[i][j] == 1:
                return True
            isClosed = True
            isClosed &= dfs(i - 1, j)
            isClosed &= dfs(i + 1, j)
            isClosed &= dfs(i, j - 1)
            isClosed &= dfs(i, j + 1)
            return isClosed
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                    isClosed = dfs(i, j)
                    if isClosed:
                        count += 1
        return count