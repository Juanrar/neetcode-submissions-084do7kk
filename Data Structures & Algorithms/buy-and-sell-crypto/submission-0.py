class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buyPrice = float("inf")

        for i in range(len(prices)):
            buyPrice = min(buyPrice, prices[i])
            if buyPrice < prices[i]:
                result = max(result, prices[i] - buyPrice)
            
        return result