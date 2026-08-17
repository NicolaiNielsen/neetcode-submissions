class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res +=  str(len(s)) + "#" + s

        return res
            

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[i] != '#':
                i += 1
            
            
            length = int(s[j:i])
            j = i + 1 + length
            res.append(s[i + 1:j])

            i = j
        return res



