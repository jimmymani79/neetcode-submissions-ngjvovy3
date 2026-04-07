class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use sliding window
        # Two pointer left, right
        # forward right
        # record max profit in each window
        # when right is less than previos move the left
        left , best = 0, 0

        for right in range(len(prices)):

            best = max(best, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
        return best
        