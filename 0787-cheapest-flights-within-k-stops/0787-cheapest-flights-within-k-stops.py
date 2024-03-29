class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            tempprices=prices.copy()
            for s,d,c in flights:
                if prices[s]==float("inf"):
                    continue
                if prices[s]+c < tempprices[d]:
                    tempprices[d]=prices[s]+c
            prices=tempprices

        return prices[dst] if prices[dst]!=float("inf") else -1            
