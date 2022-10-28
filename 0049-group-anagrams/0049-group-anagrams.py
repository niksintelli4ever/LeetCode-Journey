class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-ord("a")]+=1
            dict1[tuple(count)].append(w)
        
        return dict1.values()
            
        