class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxDiff = prices[0], 0
        for price in prices:
            maxDiff = max(maxDiff, price - minPrice)
            if price < minPrice:
                minPrice = price
        return maxDiff
