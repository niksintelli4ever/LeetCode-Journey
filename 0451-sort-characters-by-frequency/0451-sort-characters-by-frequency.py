class Solution:
    def frequencySort(self, s: str) -> str:
        dict1={}
        res=[]
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        
        heap=[[-freq,nums] for nums,freq in dict1.items()]
        heapify(heap)
        print(heap)
        while heap:
            f,v=heappop(heap)
            while f<0:
                res.append(v)
                f+=1
        return "".join(res)
        