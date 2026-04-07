class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        best = 1
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            best = max(best, right - left + 1)
            seen.add(s[right])
        return best
