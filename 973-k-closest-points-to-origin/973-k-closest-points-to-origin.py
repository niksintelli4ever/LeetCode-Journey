class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[0]*len(points)
        a=[]
        for i in range(len(points)):
            x,y=points[i]
            res[i]=math.sqrt(pow(x-0,2)+pow(y-0,2)),i
        heapify(res)
        print(res)
        for i in range(k):
            v,ind=heappop(res)
            a.append(points[ind])
        
        return a
            
        
            
        
        