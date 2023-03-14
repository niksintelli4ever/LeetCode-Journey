class Solution:
    def setZeroes(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        dontaddrows=[]
        dontaddcols=[]
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==0:
                    dontaddrows.append(r)
                    dontaddcols.append(c)
        for r in range(rows):
            for c in range(cols):
                if r in dontaddrows or c in dontaddcols:
                    board[r][c]=0
        

                    
        