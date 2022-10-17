class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict1={}
        for i in sentence:
            dict1[i]=1+dict1.get(i,0)
        if len(dict1)==26:
            return True
        return False
        
        