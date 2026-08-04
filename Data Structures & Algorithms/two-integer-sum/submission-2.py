class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,val in enumerate(nums):
            if target-val in m:
                return [m[target-val],i]
            else:
                m[val]=i
        print(m)