class Solution:
    def longestPalindrome(self, s: str) -> str:
        symbols_and_indices = {}
        max_palindrome = s[0]

        for i in range(len(s)):
            if not symbols_and_indices.get(s[i]):
                symbols_and_indices[s[i]] = [i]
            else:
                r = i
                for l in symbols_and_indices[s[i]]:
                    palindrome = self.define_palindrome_string(s[l:r+1])
                    if palindrome and len(palindrome) > len(max_palindrome):
                        max_palindrome = palindrome
                symbols_and_indices[s[i]].append(i)
        return max_palindrome

    def define_palindrome_string(self, string):
        if string[::-1] == string:
            return string
        return False


sol = Solution()
print(sol.longestPalindrome(''))
