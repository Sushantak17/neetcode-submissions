class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in numbers and diff != n:
                j = numbers.index(diff)
                return[i+1,j+1]

        