class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        count = 2
        res = money
        print(prices)
        for val in prices:
            if res >= val:
                res -= val
                count -= 1
            print(res)

            if count == 0:
                return res

        if count > 0:
            return money