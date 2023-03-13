class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1A=[0]*26
        s2A=[0]*26
        matches=0
        for i in range(len(s1)):
            s1A[ord(s1[i])-ord("a")]+=1
            s2A[ord(s2[i])-ord("a")]+=1
        
        for i in range(26):
            if s1A[i]==s2A[i]:
                matches+=1
        
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            c=s2[r]
            index=ord(c)-ord("a")
            s2A[index]+=1
            if s1A[index]==s2A[index]:
                matches+=1
            elif s2A[index]-1==s1A[index]:
                matches-=1
            c=s2[l]
            index=ord(c)-ord("a")
            s2A[index]-=1
            if s1A[index]==s2A[index]:
                matches+=1
            elif s2A[index]+1==s1A[index]:
                matches-=1
            l+=1
        return matches==26
            