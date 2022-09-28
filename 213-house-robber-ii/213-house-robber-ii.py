class Solution:
    def rob(self, nums: List[int]) -> int:
        a=max(nums[0],self.houserob(nums[1:]),self.houserob(nums[:-1]))
        return a
    def houserob(self,nums):
        rob1=0
        rob2=0
        for i in nums:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp

        return rob2
