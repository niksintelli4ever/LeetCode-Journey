class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["." for i in range(n)] for j in range(n)]
        res=[]
        cols=set()
        posd=set()
        negd=set()
        def dfs(r):
            if r==n:
                copy=["".join(i) for i in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or r+c in posd or r-c in negd:
                    continue
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                negd.remove(r-c)
                posd.remove(r+c)
                cols.remove(c)
                board[r][c]="."
            
        dfs(0)
        return res
        