class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        res=[]
        for i in arr:
            a=abs(i-x)
            heappush(heap,[a,i])
        
        for i in range(k):
            a,x=heappop(heap)
            res.append(x)
        res.sort()
        return res
        