class Solution:
    def isPalindrome(self, s: str) -> bool:
        #input - string,output-bool
        #optimal - 2 pointer

        l=0
        r=len(s)-1

        while l<r:
            while l<r and not self.check(s[l]):
                l+=1
            while r>l and not self.check(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True

    def check(self,c):
        if(ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
            return True
            

            

        