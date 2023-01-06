class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heap = costs
        heapify(heap)
        totSum = 0
        count=0
        
        while heap:
            p = heappop(heap)
            if totSum+p <=coins:
                totSum+=p
                count+=1
            else:
                break
        
        return count
        