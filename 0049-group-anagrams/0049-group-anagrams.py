class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        c=0
        maxc=0
        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-ord("a")]+=1
            hashmap[tuple(count)].append(w)
        return hashmap.values()
                