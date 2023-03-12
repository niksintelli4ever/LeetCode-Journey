class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashset=set()
        for i in s:
            if i in hashset:
                return i
            hashset.add(i)
        