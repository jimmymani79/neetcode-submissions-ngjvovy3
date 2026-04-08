class Solution:
    def isValid(self, s: str) -> bool:
        # crete a pair dictionary for finding the pair
        # Iterate through string
        # if opening type store in list
        # if closing type (find it from dictionary key list) pop the stack and check if the pair matches
        #  by end if stack is empty and return 
        if not s: return False
        pairs = {"}": "{", "]": "[", ")":"("}
        values = []
        for c in s:
            if c in ["{", "(", "["]:
                values.append(c)
            elif c in pairs and values:
                if values.pop() != pairs[c]:
                    return False
            else: # invalid string
                return False
        return not values

        