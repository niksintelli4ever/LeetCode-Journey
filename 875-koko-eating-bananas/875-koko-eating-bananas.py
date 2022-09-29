class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        minpiles=max(piles)
        while l<=r:
            mid=(l+r)//2
            res=0
            for i in piles:
                res+=math.ceil(i/mid)
            if res>h:    
                l=mid+1
            else:
                minpiles=min(mid,minpiles)
                r=mid-1
        
        return minpiles
                
        