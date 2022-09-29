class Solution:
    def climbStairs(self, n: int) -> int:
        onestep=1
        twostep=1
        for i in range(n):
            temp=onestep+twostep
            onestep=twostep
            twostep=temp
        
        return onestep