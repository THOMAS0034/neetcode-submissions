class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        var res="";
        for(var s of strs){
            res+=s.length;
            res+="#";
            res+=s;
        }
        console.log(res);
        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        var out=[];
        console.log(str)
        for(let i=0;i<str.length;i++){
            if(!isNaN(str[i])){
                var midval = "";
                var numstr=""
                var k=i;
                while((!isNaN(str[k]) && (str[k] != "#"))){
                    numstr+=str[k];
                    k++;
                }
                var index=parseInt(numstr)
                var j=k+1;
                while(index>0){
                    midval+=str[j];
                    j++;
                    index--;
                }
                out.push(midval);
                i=j-1;
            }
        }
        return out;
    }
}
