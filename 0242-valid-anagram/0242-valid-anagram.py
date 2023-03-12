class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        
        for j in t:
            dict2[j]=1+dict2.get(j,0)
        
        if dict1==dict2:
            return True
        return False
        