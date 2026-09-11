class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        postfix = 1
        prefix_array = []
        postfix_array = [0] * (len(nums))
        for i in range(len(nums)):
            prefix_array.append(prefix)
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            postfix_array[i] = postfix
            postfix *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(postfix_array[i] * prefix_array[i])

        return res

        