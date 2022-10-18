class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[(intervals[0])]
        for start,end in intervals:
            pend=res[-1][1]
            if start<=pend:
                pend=max(end,pend)
                res[-1][1]=pend
            else:
                res.append([start,end])
        return res
            
        
        