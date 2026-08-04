class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force - start with each number and find the length of the sequence and return the bigger one
        #optimal - only start the sequence if there doesnt exist the number-1 in the array
        #input - list,output-list

        if len(nums)==0:
            return 0
        visited=set(nums)
        res=[]

        for elem in nums:
            if elem-1 not in visited:
                length=1
                while((elem+length) in visited):
                    length+=1
                res.append(length)
        return max(res)
        