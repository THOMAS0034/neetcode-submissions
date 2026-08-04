class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
       var l = 0;
       var r = heights.length - 1;
       var res = [];

       while(l<r){
        const area = Math.min(heights[r],heights[l]) * (r-l);
        res.push(area);
        if(heights[l] <= heights[r]){
            l++;
        }
        else{
            r--;
        }
       } 

       return Math.max(...res);   
    }
}
