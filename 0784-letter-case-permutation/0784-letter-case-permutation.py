class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        def dfs(i,word):
            if i>=len(s):
                res.append(word)
                return
            if s[i].isalpha():
                dfs(i+1,word+s[i])
                if s[i].islower():
                    dfs(i+1,word+s[i].upper())
                if s[i].isupper():
                    dfs(i+1,word+s[i].lower())
            else:
                dfs(i+1,word+s[i])
        dfs(0,"")
        return res