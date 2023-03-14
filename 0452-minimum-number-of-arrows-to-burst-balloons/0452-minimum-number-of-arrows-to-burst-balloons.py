class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        # print(points)
        count=1
        lastEnd=points[0][1]
        for start,end in points[1:]:
            if start<=lastEnd:
                lastEnd=min(lastEnd,end)
            else:
                count+=1
                lastEnd=end
        
        return count
            
            