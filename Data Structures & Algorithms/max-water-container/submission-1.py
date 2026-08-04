class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #use two pointers - area = lenght*height, find minimum height from the pointers finds length and multiply and update the max

        l = 0
        r = len(heights)-1
        max_amount = 0 

        while l<r:
            low_height = min(heights[l],heights[r])
            distance = r - l
            max_amount = max(max_amount,low_height*distance)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return max_amount