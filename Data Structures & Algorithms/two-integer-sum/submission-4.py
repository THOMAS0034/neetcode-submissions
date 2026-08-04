class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input - array(sorted),output - indices pair
        #brute force - 2 loops for each number O(n^2)
        #optimal solution - for each number subtract the target and check wether the difference is present in the array

        subtracted_map = {}

        for index,num in enumerate(nums):
            sub_val = target - num
            if sub_val in subtracted_map:
                print(subtracted_map)
                return [subtracted_map[sub_val],index]
            else:
                print(subtracted_map)
                subtracted_map[num]=index
        


