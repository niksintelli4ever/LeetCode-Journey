class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s)):
            c=s[i]
            dict1[c]=1+dict1.get(c,0)
        for i in range(len(t)):
            c=t[i]
            dict2[c]=1+dict2.get(c,0)
        
        if dict1==dict2:
            return True
        
        return False
            
        