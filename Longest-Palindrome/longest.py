class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length palindromes, like "aba"
            len1 = self._expand_around_center(s, i, i)
            # Even length palindromes, like "abba"
            len2 = self._expand_around_center(s, i, i + 1)
            
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        # The length of the palindrome is R - L - 1
        return R - L - 1
