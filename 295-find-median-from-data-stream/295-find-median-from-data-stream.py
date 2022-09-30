class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        

    def addNum(self, num: int) -> None:
        heappush(self.small,-1*num)
        
        if self.small and self.large and -1*self.small[0]>self.large[0]:
            p=heappop(self.small)
            heappush(self.large,-1*p)
        if len(self.small)>len(self.large)+1:
            p=heappop(self.small)
            heappush(self.large,-1*p)
        if len(self.large)>len(self.small)+1:
            p=heappop(self.large)
            heappush(self.small,-1*p)
            
            
        

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-1*self.small[0]+self.large[0])/2
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()