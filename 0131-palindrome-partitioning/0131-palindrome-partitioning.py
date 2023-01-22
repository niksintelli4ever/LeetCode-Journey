class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        def dfs(i,visit):
            if i>=len(s):
                res.append(visit.copy())
                return
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if temp==temp[::-1]:
                    visit.append(temp)
                    dfs(j+1,visit)
                    visit.pop()
            
        dfs(0,[])
            
        return res
            
            