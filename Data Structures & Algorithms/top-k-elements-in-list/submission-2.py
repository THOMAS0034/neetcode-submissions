class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1
        freq_map_sorted = {a:b for a,b in sorted(freq_map.items(),key = lambda item:item[1],reverse=True)}
        res=[]
        for i,(key,val) in enumerate(freq_map_sorted.items()):
            if i == k:
                break
            else:
                res.append(key)
        return res
