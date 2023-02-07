class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict1={}
        maxlength=0
        l=0
        r=0
        while r<len(fruits):
            dict1[fruits[r]]=r
            if len(dict1)>2:
                todel=min(dict1.values())
                del dict1[fruits[todel]]
                l=todel+1
            else:
                length=r-l+1
                maxlength=max(maxlength,length)
            
            r+=1
        
        return maxlength
        