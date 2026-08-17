class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            length_of_string = ""
            while s[j] != "#":
                length_of_string += s[j]
                j += 1

            int_length = int(length_of_string)
            print(int_length)
            i = j + int_length + 1
            res.append(s[j + 1: i])
            print(res)

        return res 