class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        dict1={}
        resLen=0
        for r in range(len(fruits)):
            c=fruits[r]
            dict1[c]=1+dict1.get(c,0)
            while len(dict1)>2:
                dict1[fruits[l]]-=1
                if dict1[fruits[l]]==0:
                    del dict1[fruits[l]]
                l+=1
            resLen=max(resLen,r-l+1)
        
        return resLen
            
                
        