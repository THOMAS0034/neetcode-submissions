class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input - array of strings,output - array of subarrays with grouped anagrams
        #brute force solution - O(n^3) for each string in the array create an hashmap then for each other strings in the array create an hashmap and compare
        #optimal solution - create a unique key for the current str,update the map by appending the string to the array

        unique_map = defaultdict(list)

        for val in strs:
            unique_key = [0]*26

            for char in val:
                unique_key[ord(char) - ord('a')]+=1
            
            unique_map[tuple(unique_key)].append(val)

        return list(unique_map.values())