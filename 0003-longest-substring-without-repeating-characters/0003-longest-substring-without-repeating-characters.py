class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        hashset=set()
        for r in range(len(s)):
            c=s[r]
            while c in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(c)
            maxlen=max(r-l+1,maxlen) 
        return maxlen
        