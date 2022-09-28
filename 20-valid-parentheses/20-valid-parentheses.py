class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict1={'}':'{',')':'(',']':'['}
        for i in range(len(s)):
            if s[i] in dict1.values():
                stack.append(s[i])
            elif s[i] in dict1.keys():
                if stack==[] or stack.pop()!=dict1[s[i]]:
                    return False
        
        return stack==[]
        