class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        var s=[];
        for(var i=0;i<nums.length;i++){
            const diff = target - nums[i];
            console.log(diff);
            if(map.has(diff)){
                s.push(i,map.get(diff));
            }
            else{
                map.set(nums[i],i);
            }
        }
        return s;
    }
}
