class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # define a max best area = 0
        # iterate over the array and use left and right pointers left < right
        # record the max area (min heign * right-left +1)
        #  move the pointer where the value is small
        
        if not heights or len(heights) == 1: return 0
        left, right, best = 0, len(heights)-1, 0

        while left < right:
            min_height = min(heights[left], heights[right])
            length = right - left
            best = max(best, min_height * length)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return best


        