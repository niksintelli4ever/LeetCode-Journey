class MedianFinder:

    def __init__(self):
        self.small=[] #maxheap
        self.large=[] #minheap
        
        

    def addNum(self, num: int) -> None:
        val=-1*num
        heappush(self.small,val)
        while self.small and self.large and -1*self.small[0]>self.large[0] or len(self.small)>len(self.large)+1:
            x=heappop(self.small)
            heappush(self.large,-x)
        
        if len(self.small)>len(self.large)+1:
            x=heappop(self.small)
            heappush(self.large,-x)
        
        if len(self.large)>len(self.small)+1:
            x=heappop(self.large)
            heappush(self.small,-x)

          

    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return self.large[0]
        elif len(self.small)>len(self.large):
            return -1*self.small[0]
        else:
            return (self.large[0]+(-1*self.small[0]))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()