class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        maxlen=0
        for i in nums:
            if i not in hashset:
                hashset.add(i)
        
        for i in nums:
            if i-1 not in hashset:
                length=0
                while i+length in hashset:
                    length+=1
                maxlen=max(maxlen,length)
        
        return maxlen
                
        