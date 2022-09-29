class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0
        maxsum=max(nums)
        for i in nums:
            if sum1<0:
                sum1=0
            sum1+=i
            maxsum=max(sum1,maxsum)
        
        return maxsum
        