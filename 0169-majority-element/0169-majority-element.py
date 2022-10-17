class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        n=len(nums)
        for i in nums:
            dict1[i]=1+dict1.get(i,0)
            if dict1[i]>n/2:
                return i
            
                
        