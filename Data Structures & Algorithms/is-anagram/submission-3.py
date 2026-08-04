class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms={}
        mt={}
        for char in s:
            if char in ms:
                ms[char]+=1
            else:
                ms[char]=1
        for char in t:
            if char in mt:
                mt[char]+=1
            else:
                mt[char]=1
        for key,val in ms.items():
            if key not in mt:
                return False
            elif key in mt and ms[key] != mt[key]:
                return False
            elif len(ms)!=len(mt):
                return False
        return True
        