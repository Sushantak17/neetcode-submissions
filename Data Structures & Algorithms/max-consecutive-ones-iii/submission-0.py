class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        max_ones = 0
        while end < len(nums):
            if nums[end] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            
            end += 1
            max_ones = max(max_ones,end - start)
        return max_ones
        