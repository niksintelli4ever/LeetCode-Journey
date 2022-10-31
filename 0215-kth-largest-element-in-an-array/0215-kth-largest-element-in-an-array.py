class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[-n for n in nums]
        heapify(heap)
        for i in range(k):
            p=heappop(heap)
        
        return -p
        