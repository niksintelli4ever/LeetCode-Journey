class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def dfs(i,visit):
            if i>=len(digits):
                res.append("".join(visit.copy()))
                return
            for p in dict1[digits[i]]:
                visit.append(p)
                dfs(i+1,visit)
                visit.pop()
        
        dfs(0,[])
        return res if digits else []