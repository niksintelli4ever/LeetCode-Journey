class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(0,len(nums)):
            res=res^i
            res=res^nums[i]
        
        return res
            
        