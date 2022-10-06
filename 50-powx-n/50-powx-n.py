class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def p(x,n):
            if n==0:
                return 1
            if n%2==0:
                return p(x*x,n//2)
            elif n%2:
                return x* p(x*x,n//2)
        
        a=p(x,abs(n))
        return a if n>0 else 1/a