class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        preffix = [1]*n
        suffix = [1]*n
        for i in range(1,n):
            preffix[i]=nums[i-1]*preffix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]
        res=[0]*n
        for i in range(n):
            res[i] = preffix[i] * suffix[i]
        return res