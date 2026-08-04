class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {

        var map = {
            ')':"(",
            '}':"{",
            ']':"["
        }

        var stack = [];

        for(let c of s){
            if( !(c in map) ){
                stack.push(c);
            }

            else{
                if(stack.length === 0) return false;

                const curr = stack.pop();

                if(map[c] !== curr){
                    return false
                }
            }
        }
        return stack.length === 0;
    }
}


