class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        var sorted = nums.sort((a,b) => a -b);
        var result =[];
        var seen = new Set();
        for(let i=0;i<sorted.length;i++){
            var firstval = nums[i];
            var j = i + 1;
            var k = sorted.length - 1;
            while(j<k){
                var sum = sorted[j] + sorted[k] + firstval;
                if(sum == 0){
                var triplet = [firstval, sorted[j], sorted[k]];
                var key = triplet.join(','); 
                if (!seen.has(key)) {
                    result.push(triplet);
                    seen.add(key);
                }
                j++;
                k--;
                }
                else if(sorted[j] + sorted[k] +firstval > 0){
                k--;
                }
                else{
                j++;
                }
            }
        }
        return result;
    }
}
