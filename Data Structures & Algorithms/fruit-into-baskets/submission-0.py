class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end = 0
        max_len = 0
        d = {}
        while end < len(fruits):
            d[fruits[end]] = end
            while len(d) > 2:
                min_len = min(d.values())
                del d[fruits[min_len]]
                start = min_len + 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
    