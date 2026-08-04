class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        map_set1 = {}
        map_set2 = {}
        for char in s:
            if char in map_set1:
                map_set1[char]+=1
            else:
                map_set1[char]=1
        for char in t:
            if char in map_set2:
                map_set2[char]+=1
            else:
                map_set2[char]=1
        for key,value in map_set1.items():
            if key not in map_set2:
                return False
            elif map_set2[key] != value:
                return False
        return True
        