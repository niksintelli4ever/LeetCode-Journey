class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        hashset=set(nums)
        for i in range(1,max(hashset)+2):
            if i not in hashset:
                return i

        