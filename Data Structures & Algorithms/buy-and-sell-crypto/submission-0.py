class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        past_prices = []
        for price in prices:
            if past_prices == []:
                past_prices.append(price)
                continue
            buy = min(past_prices)
            if (price - buy) > max_profit:
                max_profit = price - buy
            past_prices.append(price)
        return max_profit