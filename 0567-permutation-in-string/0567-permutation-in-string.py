class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1M=[0]*26
        s2M=[0]*26
        matches=0
        l=0
        for i in range(len(s1)):
            s1M[ord(s1[i])-ord("a")]+=1
            s2M[ord(s2[i])-ord("a")]+=1
        for i in range(26):
            if s1M[i]==s2M[i]:
                matches+=1
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            c=s2[r]
            index=ord(c)-ord("a")
            s2M[index]+=1
            if s2M[index]==s1M[index]:
                matches+=1
            elif s2M[index]-1==s1M[index]:
                matches-=1
            
            c=s2[l]
            index=ord(c)-ord("a")
            s2M[index]-=1
            if s2M[index]==s1M[index]:
                matches+=1
            elif s2M[index]+1==s1M[index]:
                matches-=1
            l+=1
        return matches==26
            
          
        