class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        mineatingspeed=max(piles)
        while l<=r:
            eatingspeed=0
            mid=(l+r)//2
            for p in piles:
                eatingspeed+=math.ceil(p/mid)
            if eatingspeed>h:
                l=mid+1
            else:
                mineatingspeed=min(mid,mineatingspeed)
                r=mid-1
        
        return mineatingspeed