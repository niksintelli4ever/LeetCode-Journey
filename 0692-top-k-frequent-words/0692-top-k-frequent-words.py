class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1=defaultdict(int)
        for w in words:
           dict1[w]+=1
        res=[]
        res = sorted(dict1, key=lambda x: (-dict1[x], x))
        print(res)
        return res[:k]
        