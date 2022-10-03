class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        maxResLen=0
        for i in range(len(s)):
            #Even
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                resLen=r-l+1
                if resLen>maxResLen:
                    res=s[l:r+1]
                    maxResLen=max(resLen,maxResLen)
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                resLen=r-l+1
                if resLen>maxResLen:
                    res=s[l:r+1]
                    maxResLen=max(resLen,maxResLen)
                l-=1
                r+=1
        
        return res
            
            
                
        