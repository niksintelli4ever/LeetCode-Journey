class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top=0
        bottom=rows-1
        while top<=bottom:
            mid=(top+bottom)//2
            if target>matrix[mid][-1]:
                top=mid+1
            elif target<matrix[mid][0]:
                bottom=mid-1
            else:
                break
        if not top<=bottom:
            return False
        l=0
        row=(top+bottom)//2
        r=cols-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid]<target:
                l=mid+1
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                return True
        return False
            
            