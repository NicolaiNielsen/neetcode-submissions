class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #key to victory:
        # we can maintain a count for s1, then make window of size s1 and look into s2 and then compare counts and decrement and increase until we find a match. However, this is inefficient since running comparisons here is o(26) * n

        #so what we do instead is keep two counts, count the number of matches and if its even to 26 then we win.

        #init counts
        s1_count, s2_count = [0] * 26, [0] * 26
        matches = 0
        #init count and the first x (len(s1)) count of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        #count number of current matches
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            #extend the window
            index = ord(s2[i]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1

        return matches == 26
            

            

        