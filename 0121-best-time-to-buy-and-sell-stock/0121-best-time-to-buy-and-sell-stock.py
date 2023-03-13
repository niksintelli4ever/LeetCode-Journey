class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxprofit=0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            else:
                l=r
        
        return maxprofit
                
        