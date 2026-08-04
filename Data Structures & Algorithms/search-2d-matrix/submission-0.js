class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        for(let row of matrix){
            const firstidx = row[0];
            const lastidx =  row[row.length - 1];
            if(target >= firstidx && target <= lastidx){
                var r = row.length  - 1;
                var l = 0;
                while(l<=r){
                    const index = Math.floor((l+r)/2);
                    if(row[index] == target){
                        return true;
                    }
                    else if(row[index] > target){
                        r = r - 1;
                    }
                    else{
                        l = l + 1;
                    }
                } 
            }
        }
        return false;
    }
}
