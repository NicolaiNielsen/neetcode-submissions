class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        char_count = {}

        for i in range(len(s)):
            if s[i] in char_count:
                char_count[s[i]] = char_count[s[i]] + 1
            else:
                char_count[s[i]] = 1

            if t[i] in char_count:
                char_count[t[i]] = char_count[t[i]] - 1
            else:
                char_count[t[i]] = -1

            
        for value in char_count.values():
            if value != 0:
                return False

        return True

        