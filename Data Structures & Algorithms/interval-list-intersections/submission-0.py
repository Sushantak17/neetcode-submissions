class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        index1 = 0
        index2 = 0
        while index1 < len(firstList) and index2 < len(secondList):
            start = max(firstList[index1][0],secondList[index2][0])
            end = min(firstList[index1][1],secondList[index2][1])
            if start <= end:
                res.append([start,end])
            if firstList[index1][1] < secondList[index2][1]:
                index1 += 1
            else:
                index2 += 1
        return res
