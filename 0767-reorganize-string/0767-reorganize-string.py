class Solution:
    def reorganizeString(self, s: str) -> str:
        dict1={}
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        heap=[]
        res=[]
        for i,v in dict1.items():
            heappush(heap,[-v,i])
        # print(heap)
        while len(heap)>=2:
            a1,b1=heappop(heap)
            a2,b2=heappop(heap)
            a1+=1
            a2+=1
            res.append(b1)
            res.append(b2)
            if a1<0:
                heappush(heap,[a1,b1])
            if a2<0:
                heappush(heap,[a2,b2])
        
        if len(heap)==1:
            a1,b1=heappop(heap)
            if a1<=-2:
                return ""
            else:
                res.append(b1)
        
        return "".join(res)
        