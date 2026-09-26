class Solution:
    def trap(self, height: List[int]) -> int:
        #this is kinda funny, imagine we have pivot that either r or left, from each index, we subtract the current value with the maxleft or max right to get the trapped water in a specific column.
        n = len(height) - 1
        max_l = height[0]
        max_r = height[n]
        
        l = 0
        r = n
        res = 0
        while l <= r:
            if max_l < max_r:
                trapped_water = min(max_l, max_r) - height[l]
                if trapped_water > 0: 
                    res += trapped_water
                
                max_l = max(height[l], max_l)
                l += 1
            else:
                trapped_water = min(max_l, max_r) - height[r]
                if trapped_water > 0: 
                    res += trapped_water
                
                max_r = max(height[r], max_r)
                r -= 1

        return res

