class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.powcalculator(n)
            if n==1:
                return True
        return False
            
        
    
    def powcalculator(self,n):
        sum1=0
        while n>0:
            temp=n%10
            sum1+=temp**2
            n=n//10
        
        return sum1