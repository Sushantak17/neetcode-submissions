class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res = sorted(set(nums))

        longest = 1
        current = 1

        for i in range(1,len(res)):
            if res[i] == res[i-1]+1:
                current += 1

            else:
                longest = max(current,longest)
                current = 1

        return max(longest,current)

        