class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}
        for word in strs:
            word_count = [0] * 28

            for c in word:
                word_count[ord('a') - ord(c)] += 1

            key = word_count
            key = tuple(key)
            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key] = [word]
        
        return list(anagram.values())