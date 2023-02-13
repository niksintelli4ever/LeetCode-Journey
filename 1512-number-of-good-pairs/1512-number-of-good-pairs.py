class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict1={}
        count=0
        for i in nums:
            if i in dict1:
                count+=dict1[i]
                dict1[i]+=1
            else:
                dict1[i]=1
        
        return count
                
        