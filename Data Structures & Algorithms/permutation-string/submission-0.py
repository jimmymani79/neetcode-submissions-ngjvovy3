class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create an array of size 26 for all chars count
        # slide through s2 and add the chars count in another array
        ## When size is three compare them and return true if same
        ### if not matching remove the left char from the window array
        ### left ++ 
        if not s1 or not s2: return False
        if len(s1) > len(s2): return False
        if s1 == s2: return True
        s1counter = [0] * 26
        wcounter = [0] * 26
        left = 0
        for c in s1:
            s1counter[ord(c) - ord('a')] += 1
        for right in range(len(s2)):
            wcounter[ord(s2[right]) - ord('a')] += 1
            if s1counter == wcounter: return True

            if right - left +1 == len(s1):
                wcounter[ord(s2[left]) - ord('a')] -= 1
                left +=1
        return False



            



        