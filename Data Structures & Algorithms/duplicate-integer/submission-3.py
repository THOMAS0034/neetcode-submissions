class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input is array, output is bool
        # brute force = Checking each value with rest of the array O(n^2)
        # Optimal solution (time) = sacrifice space for time -> use hashmap to find duplicates
        # No edge cases to be solved

        duplicate_map = {}

        for i in range(len(nums)):
            if nums[i] in duplicate_map:
                return True
            else:
                duplicate_map[nums[i]]=1 
        return False

        
