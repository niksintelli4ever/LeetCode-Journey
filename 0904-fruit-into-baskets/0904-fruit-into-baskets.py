class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict1={}
        l=0
        maxlength=0
        for r in range(len(fruits)):
            dict1[fruits[r]]=r
            if len(dict1)>2:
                todel=min(dict1.values())
                del dict1[fruits[todel]]
                l=todel+1
            else:  
                length=r-l+1
                maxlength=max(length,maxlength)
        
        return maxlength
                
        