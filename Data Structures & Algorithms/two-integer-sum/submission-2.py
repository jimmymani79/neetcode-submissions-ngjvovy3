class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []
        if len(nums) < 2: return []
        seen = set()
        seen = {}

        for i in range(len(nums)):
            diff  = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
                # return [nums.index(diff), i]
            # seen.add(nums[i])
            seen[nums[i]] = i
        