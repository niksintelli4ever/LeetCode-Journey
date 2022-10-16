class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        z=[(p,s) for p,s in zip(position,speed)]
        z.sort()
        z=z[::-1]
        print(z)
        stack=[]
        for i,j in z:
            stack.append((target-i)/j)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)
            
            
        
        