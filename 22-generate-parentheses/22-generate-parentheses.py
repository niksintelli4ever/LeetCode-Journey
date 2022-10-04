class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def genparan(openb,closeb):
            if openb==closeb==n:
                res.append("".join(stack.copy()))
                return
            if openb<n:
                stack.append("(")
                genparan(openb+1,closeb)
                stack.pop()
            if closeb<openb:
                stack.append(")")
                genparan(openb,closeb+1)
                stack.pop()
        genparan(0,0)
        return res
            
            
        