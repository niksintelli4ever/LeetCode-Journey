class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        b=k
        res=[]
        check1=[]
        n=1
        for i,j in enumerate(arr):
            check1.append([abs(j-x),i])
        heapify(check1)
        print(check1)

        for i in range(k):
            p,q=heappop(check1)
            res.append(arr[q])
        print(res)
        res.sort()
        return res