class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input - array of numbers and target,output - list of index

        diff_map = {}
        for i in range(len(numbers)):
            diff_val = target - numbers[i]

            if diff_val in diff_map:
                return [diff_map[diff_val],i+1]
            diff_map[numbers[i]]=i+1
            

        