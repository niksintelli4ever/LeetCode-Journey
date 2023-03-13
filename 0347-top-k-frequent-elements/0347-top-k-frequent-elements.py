class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        dict1={}
        res=[]
        for i in nums:
            dict1[i]=1+dict1.get(i,0)
        for i,v in dict1.items():
            heappush(heap,[-v,i])
        
        for i in range(k):
            a,b=heappop(heap)
            res.append(b)
        return res