class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        maxres=0
        for i in nums:
            hashset.add(i)
        
        for i in nums:
            if i-1 not in hashset:
                count=0
                while i+count in hashset:
                    count+=1
                
                maxres=max(maxres,count)
        
        return maxres