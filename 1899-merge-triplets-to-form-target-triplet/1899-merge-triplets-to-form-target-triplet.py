class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        visit=set()
        for t1,t2,t3 in triplets:
            if t1>target[0] or t2>target[1] or t3>target[2]:
                continue
            if t1==target[0]:
                visit.add(0)
            if t2==target[1]:
                visit.add(1)
            if t3==target[2]:
                visit.add(3)
        
        if len(visit)==3:
            return True
        return False
        