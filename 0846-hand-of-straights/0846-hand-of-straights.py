
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        heap=[]
        dict1={}
        for i in hand:
            dict1[i]=1+dict1.get(i,0)
        minH=list(dict1.keys())
        heapify(minH)
        while minH:
            first=minH[0]
            for i in range(first,first+groupSize):
                if i not in dict1:
                    return False
                dict1[i]-=1
                if dict1[i]==0:
                    if i!=minH[0]:
                        return False
                    heappop(minH)
        return True
        