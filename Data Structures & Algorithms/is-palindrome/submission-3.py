class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers 
        # move from right and left until left < right
        # return true if end of the loop
        # return false if chars are not same
        if not s: return False
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left +=1
            while not s[right].isalnum() and right > left:
                right -= 1
            # if not s[left].isalnum():
            #     left += 1
            #     continue
            # if not s[right].isalnum():
            #     right -= 1
            #     continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True