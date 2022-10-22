class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        countt={}
        result=[-1,-1]
        count=float("infinity")
        l=0
        for i in range(len(t)):
            countt[t[i]]=1+countt.get(t[i],0)
        have=0
        need=len(countt)
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countt and window[c]==countt[c]:
                have+=1
            while have==need: 
                if (r-l+1) < count:
                    result=[l,r]
                    count=(r-l+1)
                window[s[l]]-=1
                if s[l] in countt and window[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        l,r=result
        return s[l:r+1] if count!=float("infinity") else ""
                    