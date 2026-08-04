class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap -> frequency count if more than one return false

        duplicate_map = {}

        for num in nums:
            if num in duplicate_map:
                return True
            else:
                duplicate_map[num]=1
        return False


        
