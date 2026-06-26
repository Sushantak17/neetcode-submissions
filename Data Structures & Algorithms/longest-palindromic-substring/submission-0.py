class Solution:

    def palindrome(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.palindrome(s,i,i)
            if len(odd) > len(res):
                res = odd
            even = self.palindrome(s,i,i+1)
            if len(even) > len(res):
                res = even
        return res