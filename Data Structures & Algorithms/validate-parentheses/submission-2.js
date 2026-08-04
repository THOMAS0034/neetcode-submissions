class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const map = {
            ')' : "(",
            '}' : "{",
            ']' : "["
        };

        const stack = [];

        for (let c of s) {
            if (!(c in map)) {
                stack.push(c);
            } else {
                if (stack.length === 0) return false;

                const top = stack.pop(); 
                if (map[c] !== top) {
                    return false; 
                }
            }
        }

        return stack.length === 0;
    }
}
