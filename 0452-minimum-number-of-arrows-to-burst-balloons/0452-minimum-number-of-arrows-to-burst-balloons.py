class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        previousend=points[0][1]
        res=1
        for start,end in points[1:]:
            if start<=previousend:
                previousend=min(end,previousend)
            else:
                res+=1
                previousend=end
        
        return res

        
        