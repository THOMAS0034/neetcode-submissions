class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        var r = 0;
        var l = numbers.length - 1;

        while (r<l){
            if(numbers[r] + numbers[l] == target){
                return [r+1,l+1];
            }
            else if(numbers[r] + numbers[l] > target){
                l--;
            }
            else{
                r++;
            }          
        }

    }
}
