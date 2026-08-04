class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        //quick compare for shorter lenght strings test cases
        if (s.length != t.length) { return false; }

        const maps = new Map(); //map for sting s
        const mapt = new Map(); //map for string t

        // mapping loop for string s
        for(let i=0;i<s.length;i++){
            if(maps.has(s[i])){
                maps.set(s[i],maps.get(s[i])+1);
            }
            else{
                maps.set(s[i],1);
            }
        }

        // mapping for string t
        for(let i=0;i<t.length;i++){
            if(mapt.has(t[i])){
                mapt.set(t[i],mapt.get(t[i])+1);
            }
            else{
                mapt.set(t[i],1);
            }
        }

        for(let[key,val] of maps){
            if(!mapt.has(key) || mapt.get(key) < val){
                return false
            }
        }

        return true;

    }
}
