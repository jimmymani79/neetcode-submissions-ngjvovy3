class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the list
        # iterate each element and add with left (i+1) and right (len-1)
        # if i-1 is a dupe of i skip the iteration to avoid dupes
        # start a loop for iterate 
        ## left is i+1 right is len-1
        ### if sum of i, left & right is 0 add the pairs into the result
        #### if left+1 is dupe of left skip (use a while loop)
        #### if right-1 is dupe of right skip (use a while loop)
        #### increment/decrement left and right
        
        ### if sum is < 0 left +=1
        ### if sum is > 0 right -= 1
        if not nums: return []
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    out.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1

                    left += 1
                    right -= 1

                elif sum < 0:
                    left +=1
                else:
                    right -= 1
        return out
            
                









        