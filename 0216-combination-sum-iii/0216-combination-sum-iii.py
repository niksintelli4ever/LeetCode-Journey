class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        target=n
        res=[]
        copy=[i for i in range(1,10)]
        def dfs(i,visit,t):
            if t==n and len(visit)==k:
                res.append(visit.copy())
                return
            if t>n or i>=len(copy):
                return
            visit.append(copy[i])
            dfs(i+1,visit,t+copy[i])
            visit.pop()
            dfs(i+1,visit,t)
        dfs(0,[],0)
        return res
            
        