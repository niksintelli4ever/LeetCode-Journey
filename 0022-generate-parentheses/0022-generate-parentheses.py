class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        visit=[]
        res=[]
        def dfs(openB,closeB):
            if openB==closeB==n:
                res.append("".join(visit.copy()))
                return
            if openB<n:
                visit.append("(")
                dfs(openB+1,closeB)
                visit.pop()
            if closeB<openB:
                visit.append(")")
                dfs(openB,closeB+1)
                visit.pop()
        
        dfs(0,0)
        return res
            
        