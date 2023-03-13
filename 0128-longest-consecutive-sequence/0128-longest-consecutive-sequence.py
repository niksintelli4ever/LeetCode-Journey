class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        maxcount=0
        for i in nums:
            if i-1 not in hashset:
                count=0
                while i+count in hashset:
                    count+=1
                maxcount=max(count,maxcount)
        return maxcount
        