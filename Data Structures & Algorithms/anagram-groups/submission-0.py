class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we use defaultdict so that if we try to append a value whose key
        # doesn't exist, it doesn't throw error
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                # ord() gives ASCII/Unicode value of character
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())