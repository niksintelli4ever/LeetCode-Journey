class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[0]*len(points)
        res=[]
        for i in range(len(points)):
            x,y=points[i]
            a[i]=sqrt(pow(x-0,2)+pow(y-0,2)),i
        
        heapify(a)
        for i in range(k):
            x,y=heappop(a)
            res.append(points[y])
        
        return res
        
        
            
            
            
        
        