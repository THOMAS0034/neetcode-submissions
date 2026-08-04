class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #input - 2 strings,output-bool
        #brute force - O(n^2) -> compare each char in a string with each char in other string
        #optimal solution - store count of each char in a hashmap and after iterating the other string check for availablity of the current char in the hashmap
        #problems - one string can have duplicate characters and other can have a single char of the same
        #edge cases - 

        if len(s)!=len(t):return False
        character_map = {}
        for char in s:
            if char in character_map:
                character_map[char]+=1
            else:
                character_map[char]=1
        print(character_map)

        condition = False

        for char in t:
            if char in character_map and character_map[char] > 0:
                character_map[char]-=1
                condition = True
            else:
                return False

        print(condition)

        return condition


        