class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input - array nums,output-array of nums
        #brute - 2 loops find product for one element for each of the other elements
        #optimal - find prefix and suffix product for each element and multiply them

        nums_length = len(nums)

        prefix = [1]*nums_length
        suffix = [1]*nums_length

        res=[]

        for i in range(1,nums_length):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(nums_length-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        for i in range(nums_length):
            res.append(prefix[i] * suffix[i])

        return res



        