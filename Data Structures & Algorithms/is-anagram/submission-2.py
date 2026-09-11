class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_array_s = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            frequency_array_s[s[i]] = frequency_array_s.get(s[i], 0 ) + 1
            frequency_array_s[t[i]] = frequency_array_s.get(t[i], 0 ) - 1

        for key, value in frequency_array_s.items():
            if value != 0:
                return False

        return True

        