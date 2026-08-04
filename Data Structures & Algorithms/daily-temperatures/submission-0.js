class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const n = temperatures.length;
        var res = new Array(n).fill(0);
        const stack = [];

        for (let i = 0; i<n; i++){
            console.log(i);
            const t = temperatures[i];
            while(stack.length > 0 && t > stack[stack.length -1][0]){
                const [,stackindx] = stack.pop();
                res[stackindx] = i - stackindx
            }
            stack.push([temperatures[i],i])
        }
        return res;
    }
}
