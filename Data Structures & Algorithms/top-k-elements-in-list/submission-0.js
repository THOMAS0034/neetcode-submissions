class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();

        //create a hashmap with the frequencies of every integer
        for(var num of nums){
            if(map.has(num)){
                map.set(num,map.get(num)+1);
            }
            else{
                map.set(num,1);
            }
        }

        //sort the map with spread operator and .entries() method to get it as array
        const sort = [...map.entries()].sort((a,b) => b[1]-a[1]);

        var res=[];
        for(let i=0;i<k;i++){
            //push the element for k most elements
            res.push(sort[i][0]);
        }
        return res;
    }
}
