class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            if char in m:
                stack.append(m[char])
            elif stack and char == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
        