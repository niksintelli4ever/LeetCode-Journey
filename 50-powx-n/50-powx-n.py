class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def powmy(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            if n%2==0:
                res=powmy(x*x,n//2)
            else:
                res= x*powmy(x*x,n//2)
            
            return res
        res=powmy(x,abs(n))
        return res if n>=0 else 1/res
            
            