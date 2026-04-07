class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[2,20,4,10,3,4,5]
        # Move the items into a set O(N)
        # iterate over the array 
        # if n-1 is found skip there
        # if n-1 not there look for n+1 exist and start a loop until the chain break
        ## keep the max count
        if not nums: return 0
        best = 1
        nums_set = set(nums)
        for index, n in enumerate(nums):
            if n-1 in nums_set:
                continue
            current_cnt  = 1
            while n+1 in nums_set:
                n += 1
                current_cnt += 1
            best = max(current_cnt, best)
        return best
