class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapify(heap)
        if len(heap)==1:
            return -1*heap[0]
        while len(heap)>=2:
            p=-1*heappop(heap)
            q=-1*heappop(heap)
            if p==q:
                continue
            elif p>q:
                c=p-q
                c=-1*c
                heappush(heap,c)
        print(heap)
        return -1*heap[0] if heap else 0 
        