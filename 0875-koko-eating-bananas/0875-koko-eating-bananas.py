class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        eatingspeed=max(piles)
        while l<=r:
            mid=(l+r)//2
            f=0
            for p in piles:
                f+=math.ceil(p/mid)
            if f>h:
                l=mid+1
            else:
                eatingspeed=min(eatingspeed,mid)
                r=mid-1
        
        return eatingspeed
        