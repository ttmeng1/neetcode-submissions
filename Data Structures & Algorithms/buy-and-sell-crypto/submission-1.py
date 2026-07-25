class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        past_prices = []
        for price in prices: # let current price be selling price
            if past_prices == []: # append first price to past prices, can't sell first day
                past_prices.append(price)
                continue
            buy = min(past_prices) # find lowest buying price in past prices
            if (price - buy) > max_profit: # check if profit is higher
                max_profit = price - buy
            past_prices.append(price)
        return max_profit