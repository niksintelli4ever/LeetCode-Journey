class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0 for i in range(len(temperatures))]
        for i,j in enumerate(temperatures):
            while stack and stack[-1][1]<j:
                stacki,stackv=stack.pop()
                res[stacki]=i-stacki
            stack.append([i,j])
        
        return res
                
                
                
        