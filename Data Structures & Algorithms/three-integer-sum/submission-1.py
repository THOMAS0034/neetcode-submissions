class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute - 3 nested for loops
        #optimal -> find 2sum and check for difference of that number

        result = set()
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                target = -(nums[i]+nums[j])
                if target in seen:
                    triplet = tuple(sorted([nums[i],nums[j],target]))
                    result.add(triplet)
                seen.add(nums[j])

        return list(result)
            
            