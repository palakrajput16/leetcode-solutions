"""
Problem: 3210. Find the Encrypted String

Difficulty: Easy

Topic:
- String

Approach:
For each position i, replace the current character with the
character located k positions ahead in the string.

Since the movement is cyclic, use modulo (%) to wrap around
when the index goes beyond the end of the string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        result = []

        n = len(s)

        for i in range(n):
            result.append(s[(i + k) % n])

        return "".join(result)