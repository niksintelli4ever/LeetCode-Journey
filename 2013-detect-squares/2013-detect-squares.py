class DetectSquares:

    def __init__(self):
        self.list=[]
        self.dict1=defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.list.append(point)
        self.dict1[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.list:
            if abs(px-x)!=abs(py-y) or px==x or py==y:
                continue
            res+=self.dict1[(x,py)]*self.dict1[(px,y)]
        
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)