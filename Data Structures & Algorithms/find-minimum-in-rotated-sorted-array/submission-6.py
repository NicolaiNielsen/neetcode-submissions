class Solution:
    def findMin(self, nums: List[int]) -> int:


        l = 0
        r = len(nums) - 1
        minimum_value = float('inf')
        while l <= r:
            m = (l + r) // 2
            current_value = nums[m]
            if nums[l] >= nums[r]:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1

            
            minimum_value = min(minimum_value, current_value)

        return minimum_value
            

        