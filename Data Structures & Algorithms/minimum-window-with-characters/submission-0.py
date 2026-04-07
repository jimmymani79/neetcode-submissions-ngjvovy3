from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # right and left
        # if left is not in t slide left side > 
        # if left in t compare for each right until all t is found
        ## record the window and continue and compare with next substring and store the best
        if not s or not t:
            return ""

        tc = Counter(t)
        wc = Counter()
        left = 0
        best = ""

        for right in range(len(s)):
            wc[s[right]] += 1

            while tc <= wc:
                if not best or (right - left + 1) < len(best):
                    best = s[left:right+1]
                wc[s[left]] -= 1
                left += 1

        return best
                
        




        