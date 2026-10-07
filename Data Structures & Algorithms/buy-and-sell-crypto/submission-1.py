class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_seen = float("inf")
        value = 0

        for price in prices:
            value = max(value, price - minimum_seen)
            minimum_seen = min(price, minimum_seen)

        return value



        