# runtime complexity: O(n)
# spactime complexity: O(1) because we do not use an additional data structures
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = 0
        for i, value in enumerate(prices):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit
        
        