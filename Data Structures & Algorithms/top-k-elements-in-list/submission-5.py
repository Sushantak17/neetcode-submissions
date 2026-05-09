class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1

        sorted_freq = sorted(freqMap.items(),
                     key=lambda x: x[1],
                     reverse=True)

        top_k = []

        for key, value in sorted_freq[:k]:
            top_k.append(key)

        return top_k