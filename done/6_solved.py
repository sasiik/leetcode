class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s[0]

        n = len(s)

        def search(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1:r]

        ret = s[0]

        for i in range(n):
            odd = search(i, i)
            even = search(i, i + 1)

            if len(odd) > len(ret):
                ret = odd

            if len(even) > len(ret):
                ret = even

        return ret
