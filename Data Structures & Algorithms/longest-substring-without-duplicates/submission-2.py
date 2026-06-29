class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        max_size = 0
        for j in range(len(s)):
            if s[j] not in window:
                window = window + s[j]
                j += 1
            else:
                while s[j] in window:
                    window = window[1:]
                window = window + s[j]
            max_size = max(max_size, len(window))
        return max_size