class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        list1 = []
        for i in range(len(rocks)):
            list1.append(capacity[i]-rocks[i])
        count = 0
        list1.sort()
        print(list1)
        for i in list1:
            if i<=additionalRocks:
                count+=1
                additionalRocks-=i
        
        return count
                
            