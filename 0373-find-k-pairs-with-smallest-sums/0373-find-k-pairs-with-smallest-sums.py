class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]
        for i in range(0,min(k,len(nums1))):
            for j in range(0,min(k,len(nums2))):
                x=nums1[i]
                y=nums2[j]
                
                total=x+y
                
                if len(heap)<k:
                    heapq.heappush(heap,[-total,x,y])
                else:
                    if total>-heap[0][0]:
                        break
                    
                    heapq.heappush(heap,[-total,x,y])
                    heapq.heappop(heap)
        
        res=[]
        while heap:
            p=heappop(heap)
            res.append([p[1],p[2]])
        
        return res