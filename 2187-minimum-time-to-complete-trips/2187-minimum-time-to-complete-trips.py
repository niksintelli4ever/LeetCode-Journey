class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l=1
        r=100000000000001
        ans=-1
        while l<=r:
            curtrip=0
            mid=l+(r-l)//2
            for i in time:
                curtrip+=mid//i
            if curtrip>=totalTrips:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        
        return ans
                
                
        
            
                    