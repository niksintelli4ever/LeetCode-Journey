class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        rev=0
        while x>0:
            temp=x%10
            rev=rev*10+temp
            x=x//10
        
        return rev==y
        