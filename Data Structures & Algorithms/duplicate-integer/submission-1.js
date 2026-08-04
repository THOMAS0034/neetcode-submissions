class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const map = new Map();
        for (var i=0;i<nums.length;i++){
            if (map.has(nums[i])){ 
                map.set(nums[i],map.get(nums[i])+1);
            }
            else{
                map.set(nums[i],1);
            }
        }
        console.log(map)
        const res=0;
        for (let [key,val] of map){
            if(val>1){
                return true;
            }
        }
        return false;
    }
}
