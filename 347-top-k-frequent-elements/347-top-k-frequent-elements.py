class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        res=[]
        for i in nums:
            hashmap[i]=1+hashmap.get(i,0)
        heap=[[-freq,nums] for nums,freq in hashmap.items()]
        heapify(heap)
        for i in range(k):
              p,q=heappop(heap)
              res.append(q)
        
        return res
              
        
    