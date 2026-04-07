from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use sliding window
        # Add each right letters into a Dict with count
        # Identify a difference betweem most freq and length. 
        # if diff is less than k keep increasing Right
        # maintain a count of most freq
        # if diff is > k , increase left untiland reduce the count from the Dict
        left = 0
        best = 1
        count = defaultdict(int)
        most_freq = 0
        total = 0
        for right in range(len(s)):
            count[s[right]] += 1
            most_freq = max(most_freq, count[s[right]])

            if (right - left + 1) - most_freq > k:
                count[s[left]] -= 1
                left += 1
            total = max(total, right-left+1)
        return total
            

        