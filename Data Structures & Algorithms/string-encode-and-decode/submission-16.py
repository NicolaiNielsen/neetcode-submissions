class Solution:
    #Encode converts data into another representation
    def encode(self, strs: List[str]) -> str:
        #string_length#full_string
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            k = int(length) + i + 1
            decoded_strs.append(s[i + 1:k])

            i = k

        return decoded_strs

            