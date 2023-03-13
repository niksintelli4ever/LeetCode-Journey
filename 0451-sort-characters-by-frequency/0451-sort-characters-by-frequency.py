import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dict1={}
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        res=[]
        heap=[]
        for i,j in dict1.items():
            heapq.heappush(heap,[-j,i])
        while heap:
            p,q=heappop(heap)
            while p<0:
                res.append(q)
                p+=1
        
        return "".join(res)
        
        