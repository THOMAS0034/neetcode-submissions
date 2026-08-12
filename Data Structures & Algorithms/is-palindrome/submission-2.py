class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        def check_ascii(char):
            if (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or 
            ord('0') <= ord(char) <= ord('9')):
                return True
            return False
            
        while start <= end:
            while start < end and check_ascii(s[start]) == False:
                start+=1
            while end > start and check_ascii(s[end]) == False:
                end-=1
            print(s[start],s[end])
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1

        return True

            

        