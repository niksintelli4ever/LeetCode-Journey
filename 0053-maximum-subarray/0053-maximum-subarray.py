class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=max(nums)
        sum1=0
        for i in range(len(nums)):
            if sum1<0:
                sum1=0
            sum1+=nums[i]
            res=max(res,sum1)
        
        return res
            
        