class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            mn = min(mn, prices[i])
            maxprofit = max(maxprofit, prices[i] - mn)       
        return maxprofit