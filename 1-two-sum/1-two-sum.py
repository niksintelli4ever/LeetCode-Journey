class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum1=0
        dict1={}
        for i in range(len(nums)):
            sum1=target-nums[i]
            if sum1 in dict1:
                return [dict1[sum1],i]
            else:
                dict1[nums[i]]=i
    
    