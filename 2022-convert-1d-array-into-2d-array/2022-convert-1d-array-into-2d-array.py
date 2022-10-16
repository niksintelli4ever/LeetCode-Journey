class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)>m*n or len(original) < m*n:
            return []
        newarray=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if original:
                    val=original.pop(0)
                    newarray[i][j]=val
        
        return newarray
                
            
            
        