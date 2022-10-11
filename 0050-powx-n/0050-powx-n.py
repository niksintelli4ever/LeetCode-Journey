class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powxn(x,n):
            if n==0:
                return 1
            if n%2:
                return x*powxn(x*x,n//2)
            else:
                return powxn(x*x,n//2)
        
        a=powxn(x,abs(n))
        return a if n>0 else 1/a
    
                
                
        