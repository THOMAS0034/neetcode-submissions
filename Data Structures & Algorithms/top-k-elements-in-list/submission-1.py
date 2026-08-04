class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input - array,output-array of elements that satisfies the condition
        #brute solution - create hashmap according to the frequency,sort it and return the k most elements
        #bucket sort - instead of sorting the hashmap create buckets for the frequency of the elements and return from the bottom to the top until k

        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1
        
        buckets=[]

        for i in range(len(nums)+1):
            buckets.append([])

        for num,freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

