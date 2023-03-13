class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res=0
        total=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(cost)):
            total+=gas[i]-cost[i]
            if total<0:
                res=i+1
                total=0
        
        return res
        
        