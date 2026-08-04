class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #define a hashset which maps the occurance of each number in the given array
        hash_set={}
        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set[i]=1
        return False        