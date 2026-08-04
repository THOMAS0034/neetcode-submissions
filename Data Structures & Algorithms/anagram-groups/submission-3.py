class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            counter = [0]*26
            for ch in word:
                counter[ord(ch) - ord('a')]+=1
            counter_key = '#'.join(map(str,counter))
            anagram_map[counter_key].append(word)

        res=[]
        for values in anagram_map.values():
            res.append(values)
        print(res)
        return res
