class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        n = len(strs)
        encoded_string += str(n) + ","
        for s in strs:
            l = len(s)
            encoded_string += str(l) + ","
        for s in strs:
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        first_comma_index = s.index(",")
        length = int(s[0:first_comma_index])
        count = 0
        char = first_comma_index + 1
        list_indices = []
        
        while count < length:
            if s[char] == ",":
                count += 1
            else:
                if count == len(list_indices):
                    list_indices.append(0)
                list_indices[-1] = list_indices[-1] * 10 + int(s[char])
            char += 1

        for word_break in list_indices:
            decoded_string.append(s[char:char+word_break])
            char += word_break
            
        return decoded_string