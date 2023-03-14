class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        z= [[t,s] for t,s in zip(position,speed)]
        z.sort(key=lambda x:x[0])
        z=z[::-1]
        print(z)
        stack=[]
        for p,s in z:
            time = (target-p)/s
            stack.append(time)
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)
        