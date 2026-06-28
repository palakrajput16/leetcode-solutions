"""
Problem: 5. Longest Palindromic Substring

Difficulty: Medium

Topic:
- String
- Two Pointers

Approach:
Treat every character (and every gap between two characters)
as the center of a potential palindrome. Expand outward from
each center while the characters on both sides are equal.
Keep track of the longest palindrome found during the process.

This approach handles both odd-length and even-length
palindromes without generating all substrings.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            #odd length palindrome
            len1 = self.expand(s, i , i)

            #even lenght palindrome
            len2 = self.expand(s, i, i+1)

            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
        