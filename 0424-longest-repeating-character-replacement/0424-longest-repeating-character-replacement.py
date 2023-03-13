class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        l=0
        maxlength=0
        for r in range(len(s)):
            c=s[r]
            dict1[c]=1+dict1.get(c,0)
            while (r-l+1 - max(dict1.values())>k):
                dict1[s[l]]-=1
                l+=1
            length=r-l+1
            maxlength=max(length,maxlength)
        return maxlength
        
        