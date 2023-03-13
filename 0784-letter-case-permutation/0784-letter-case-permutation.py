class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        def dfs(i,visit):
            if len(visit)==len(s):
                res.append("".join(visit.copy()))
                return
            if i>=len(s):
                return
         
            for j in range(i,len(s)):
                if s[j].isalpha():
                    visit.append(s[j])
                    dfs(j+1,visit)
                    visit.pop()
                    if s[j].isupper():
                        visit.append(s[j].lower())
                        dfs(j+1,visit)
                        visit.pop()
                    else:
                        visit.append(s[j].upper())
                        dfs(j+1,visit)
                        visit.pop()
                else:
                    visit.append(s[j])
                    dfs(j+1,visit)
                    visit.pop()
        dfs(0,[])
        return res
        