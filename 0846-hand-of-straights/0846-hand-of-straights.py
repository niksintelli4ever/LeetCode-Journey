class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dict1={}
        if len(hand)% groupSize:
            return False
        res=[]
        for i in hand:
            dict1[i]=1+dict1.get(i,0)
        heap=list(dict1.keys())
        heapify(heap)
        while heap:
            a=heap[0]
            for i in range(a,a+groupSize):
                if i not in dict1:
                    return False
                dict1[i]-=1
                if dict1[i]==0:
                    if i!=heap[0]:
                        return False
                    heappop(heap)
        
        return True
                
        