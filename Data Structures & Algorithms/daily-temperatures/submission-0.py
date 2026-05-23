class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            found = False
            for j in range(i+1,len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    found = True
                    res.append(count)
                    break
            if not found:
                res.append(0)
        return res