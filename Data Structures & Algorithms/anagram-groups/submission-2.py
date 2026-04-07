class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return [[""]]
        anagrams = {}
        for txt in strs:
            sort_txt = "".join(sorted(txt))
            anagrams.setdefault(sort_txt, []).append(txt)
        return list(anagrams.values())