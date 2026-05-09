#For each word, we created a frequency array of size 26 to count how many times each alphabet appears.
#We converted this count array into a tuple and used it as a hashmap key because all anagrams produce the same character frequency.
#Strings with the same frequency key were stored together in the same list/group.


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