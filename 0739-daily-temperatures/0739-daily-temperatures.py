class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                stacki,stackv=stack.pop()
                res[stacki]=i-stacki
            stack.append([i,temperatures[i]])
        
        return res
            