class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window_size = len(nums) - k + 1
        for i in range(window_size):
            max_elem = nums[i]
            for j in range(i,i+k):
                max_elem = max(nums[j],max_elem)

            res.append(max_elem)
        return res