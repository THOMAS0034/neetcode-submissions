class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

    isAlphanumeric(char) {
        return (
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z') ||
            (char >= '0' && char <= '9')
        );
    }
    isPalindrome(s) {
        var firsti = 0;
        var lasti = s.length - 1;
        while(firsti < lasti){
            while(firsti<lasti && !this.isAlphanumeric(s[firsti])){firsti++;};
            while(firsti<lasti && !this.isAlphanumeric(s[lasti])){lasti--;};

            if(s[firsti].toLowerCase() != s[lasti].toLowerCase()){
                return false;
            }
            firsti++;
            lasti--;
        }
        return true;
    }
}
