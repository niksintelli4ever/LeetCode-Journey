class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            hashmap[i]=1+hashmap.get(i,0)
            if hashmap[i] > len(nums)//2:
                return i
        