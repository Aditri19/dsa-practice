class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, profit = prices[0], 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price-buy)
        return profit