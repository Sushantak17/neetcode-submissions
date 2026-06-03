class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,n in enumerate(nums):
            # if current number is same as previous number, skip
            if i > 0 and nums[i] == nums [i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = n + nums[l] + nums[r]
                if target > 0:
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    while l < r and nums[r] == nums[r + 1]:
                        r-=1

        return res


            