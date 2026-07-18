class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        min_len = len(nums) + 1
        curr_sum = 0
        while end < len(nums):
            curr_sum += nums[end]
            end += 1
            while curr_sum >= target:
                min_len = min(min_len,end - start)
                curr_sum -= nums[start]
                start += 1
        
        return min_len if min_len != (len(nums) + 1) else 0