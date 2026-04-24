class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set and add each and look for duplicate
        if not nums: return False
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


        