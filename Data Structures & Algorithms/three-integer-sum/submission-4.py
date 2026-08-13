class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)-1
        res=[]
        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            first_number = nums[i]
            j=i+1
            k=n
            while j<k:
                threesum = first_number + nums[j] + nums[k]
                if threesum > 0:
                    k-=1
                elif threesum <0:
                    j+=1
                else:
                    res.append([first_number,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return res
        
            
            