class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_prices = prices[0]
        max_pro = 0
        for i in range(1,len(prices)):
            min_prices = min(min_prices, prices[i])
            max_pro = max(max_pro, prices[i] - min_prices)
        return max_pro
