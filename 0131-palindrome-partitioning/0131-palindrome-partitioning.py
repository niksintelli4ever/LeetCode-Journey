class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def dfs(i,t):
            if i==len(s):
                res.append(t.copy())
                return
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if temp==temp[::-1]:
                    t.append(temp)
                    dfs(j+1,t)
                    t.pop()
            
        dfs(0,[])
        return res
        