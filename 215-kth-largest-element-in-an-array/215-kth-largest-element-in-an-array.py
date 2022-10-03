class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dict1={}
        res=[]
        heap=[-i for i in nums]
        heapify(heap)
        for i in range(k):
            p=heappop(heap)
            res.append(-1*p)
        print(res)
        return res[-1]