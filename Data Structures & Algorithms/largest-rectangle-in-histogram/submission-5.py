class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                max_area = max(max_area, (i - index) * h)
                start = index

            stack.append((start, height))

        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - index))

        return max_area