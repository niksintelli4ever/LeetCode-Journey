class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            c=nums[i]
            t1=target-c
            if t1 in hashmap:
                return [i,hashmap[t1]]
            else:
                hashmap[c]=i
    
        