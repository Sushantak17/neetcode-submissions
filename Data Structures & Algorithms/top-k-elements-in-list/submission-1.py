class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        frequentList = []

        for n in nums:
            freq[n] += 1

        sorted_d = dict(sorted(freq.items()))

        top_k = [key for key, value in sorted(freq.items(),
                                      key=lambda x: x[1],
                                      reverse=True)[:k]]
        
        # for key, value in freq.items():
        #     if value >= k:
        #         frequentList.append(key)

        return top_k
            

        