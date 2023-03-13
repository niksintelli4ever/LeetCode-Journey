class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1={}
        heap=[]
        for i in tasks:
            dict1[i]=1+dict1.get(i,0)
        for i,v in dict1.items():
            heappush(heap,-v)
        time=0
        q=deque()
        while heap or q:
            time+=1
            if heap:
                a=heappop(heap)
                a+=1
                if a<0:
                    q.append([a,time+n])
            
            if q and q[0][1]==time:
                heappush(heap,q.popleft()[0])
        
        return time
            