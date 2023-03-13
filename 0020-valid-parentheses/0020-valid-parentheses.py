class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict1={")":"(","}":"{","]":"["}
        for i in s:
            if i in dict1.values():
                stack.append(i)
            elif i in dict1.keys():
                if stack==[] or stack.pop()!=dict1[i]:
                    return False
        
        return stack==[]
        