from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        for c in t:
            if c not in map:
                return False
            map[c] -= 1
            if map[c] < 0:
                return False
        return all(val == 0 for val in map.values())