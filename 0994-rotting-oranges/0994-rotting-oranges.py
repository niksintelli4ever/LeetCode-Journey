class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        time=0
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
                else:
                    continue
        r=0
        c=0
        while q and fresh > 0:
            for i in range(len(q)):
                p,e=q.popleft()
                for i,j in directions:
                    r,c=p+i,e+j
                    if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                        continue
                    grid[r][c]=2
                    fresh-=1
                    q.append((r,c))

            
            time+=1
                
        return time if fresh==0 else -1
            
                    
        