class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for c in s:
            map_s[c] = 1 + map_s.get(c,0)
        
        for c in t:
            map_t[c] = 1 + map_t.get(c,0)

        if map_t == map_s:
            return True
        else:
            return False