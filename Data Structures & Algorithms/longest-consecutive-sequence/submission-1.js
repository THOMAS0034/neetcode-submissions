class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const array = new Set(nums);
        let max = 0;

        for(let num of array){
            if(!array.has(num-1)){
                let currentnum = num;
                let currentlen = 1;

                while(array.has(currentnum+1)){
                    currentnum++;
                    currentlen++;
                }

                max = Math.max(currentlen,max)
            }
        }
        return max;

    }
}
