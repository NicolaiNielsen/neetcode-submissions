class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_eating_speed = max(piles)
        l = 1
        r = max_eating_speed
        res = float("inf")
        while l <= r:
            k = (l + r) // 2
            eating_speed = 0
            for pile in piles:
                eating_speed += (pile + k - 1) // k
            
            if eating_speed <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res