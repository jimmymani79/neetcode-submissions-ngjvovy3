from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = [0] * k
        for i in range(k):
            best_v = 0
            best_k = -1

            for key, value in c.items():
                if value > best_v:
                    best_v = value
                    best_k = key
            res[i] = best_k
            c.pop(best_k)
        return res





        