class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1={}
        for i in tasks:
            dict1[i]=1+dict1.get(i,0)
        # print(dict1)
        heap=[]
        time=0
        for i,j in dict1.items():
            heappush(heap,-j)
        q=deque()
        while heap or q:
            time+=1
            if heap:
                x=heappop(heap)+1
                if x<0:
                    q.append([x,n+time])
            if q and q[0][1]==time:
                heappush(heap,q.popleft()[0])
        return time
                
        