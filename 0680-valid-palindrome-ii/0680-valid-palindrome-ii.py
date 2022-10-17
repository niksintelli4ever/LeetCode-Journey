class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipleft=s[l+1:r+1]
                print(skipleft)
                print(r+1)
                skipright=s[l:r]
                print(r)
                print(skipright)
                print(skipright[::-1])
                return (skipleft[::-1]==skipleft or skipright[::-1]==skipright)
            l+=1     
            r-=1
        return True
                