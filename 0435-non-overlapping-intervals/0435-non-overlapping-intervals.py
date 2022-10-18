class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        prevEnd=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            if start<prevEnd:
                count+=1
                prevEnd=min(end,prevEnd)
            else:
                prevEnd=end
                

                prevEnd=end
        
        return count
            
        