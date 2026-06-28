class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = {}
        ans = []
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in anagram_list:
                anagram_list[sorted_string].append(s)
            else:
                anagram_list[sorted_string] = [s]
        return list(anagram_list.values())