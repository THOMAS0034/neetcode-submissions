class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        var l = 0;
        var r = nums.length - 1;

        while(l<=r){
            const val = Math.floor((l+r)/2);
            if(nums[val] == target){
                return val;
            }
            else if(nums[val] > target){
                r = val -1;
            }
            else{
                l = val +1;
            }
        }

        return -1;
    }
}
