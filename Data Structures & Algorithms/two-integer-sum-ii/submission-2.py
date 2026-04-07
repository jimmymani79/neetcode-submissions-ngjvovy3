class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # take the diff between current number and target 
        # if diff in seen find the index of element from numbers(this returns the first index from list)
        ##  and the current  index (return +1 for index as its expecting 1-indexed)

        # seen = set()
        
        # for i in range (len(numbers)):
        #     if target-numbers[i] in seen:
        #         return [numbers.index(target-numbers[i]) +1 , i+1]
        #     seen.add(numbers[i])
        left , right = 0 , len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left +=1
            else:
                right -=1
        return []
        