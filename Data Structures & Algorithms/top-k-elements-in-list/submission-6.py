class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        buckets=[[]for _ in range(len(nums)+1)]
        for key,val in freq_map.items():
            buckets[val].append(key)
        res=[]
        for i in range(len(nums),0,-1):
            for val in buckets[i]:
                res.append(val)
                if len(res)==k:
                    return res
            