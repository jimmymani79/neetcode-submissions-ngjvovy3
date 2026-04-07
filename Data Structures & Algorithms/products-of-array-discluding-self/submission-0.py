class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4]
        #For N solution without division we could multiply all to the left and to the right of i
        # define an output list first 
        # use two loops to find the left numbers product and right numbers product and multiple each to the output
        output = [1] * len(nums)
        left_prod = 1
        for i in range(len(nums)):
            output[i] *= left_prod
            left_prod *= nums[i]
        
        right_prod =1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]
        print(output)
        return output

             

        