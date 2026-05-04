class Solution:
    # A set uses a hash function which instantly computes exactly which memory slot that number
    # lives in. So when you ask "is 5 in this set?" — Python computes the
    # hash of 5, goes directly to that memory slot, done. Doesn't matter
    # if the set has 10 elements or 10 million. Always O(1).
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if(num in seen):
                return True
            seen.add(num)
        return False
        