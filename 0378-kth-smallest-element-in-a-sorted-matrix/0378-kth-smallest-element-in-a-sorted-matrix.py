class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row=len(matrix)
        col=len(matrix[0])
        heap=[]
        for r in range(row):
            for c in range(col):
                heapq.heappush(heap,-matrix[r][c])
                
                if len(heap)>k:
                    heappop(heap)
        
        return -heap[0]
                