class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for i in range(0,len(nums)):
            res[i] = 1
            for j in range(0,len(nums)):
                if i!=j:
                    res[i] *= nums[j]
        return res


        