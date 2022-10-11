class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        time=0
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        while q and fresh>0:
            for i in range(len(q)):
                dx,dy=q.popleft()
                for x,y in directions:
                    r,c=dx+x,dy+y
                    if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                        continue
                    grid[r][c]=2
                    q.append([r,c])
                    fresh-=1
                    
            time+=1
        return time if fresh==0 else -1