class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        frequency_count = {}

        for num in nums:
            frequency_count[num] = frequency_count.get(num, 0) + 1

        for key, value in frequency_count.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                for value in bucket[i]:
                    res.append(value)
                    if len(res) == k:
                        return res
