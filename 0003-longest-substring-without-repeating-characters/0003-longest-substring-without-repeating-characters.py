class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        l=0
        maxlength=0
        for r in range(len(s)):
            c=s[r]
            while c in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(c)
            length=r-l+1
            maxlength=max(maxlength,length)
        return maxlength
            
            
        