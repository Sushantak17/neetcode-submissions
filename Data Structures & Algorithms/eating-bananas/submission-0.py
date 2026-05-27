class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            hours = 0
            mid = (low + high) // 2
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        
        return low