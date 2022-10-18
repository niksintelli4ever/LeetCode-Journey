class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        x=[2,3,4,5,6,8,9,10]
        for i in x:
            while n%i==0:
                n=n/i
        return n==1
            
        