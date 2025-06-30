class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - current_min)
            current_min = min(current_min, price)

        return max_profit