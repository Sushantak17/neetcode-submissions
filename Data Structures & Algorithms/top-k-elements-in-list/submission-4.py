class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1

        top_k = [key for key,value in sorted(freqMap.items(),
                                            key = lambda x:x[1],
                                            reverse = True)[:k]]

        return top_k