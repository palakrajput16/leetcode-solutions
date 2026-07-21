"""
Problem: 3110. Score of a String

Difficulty: Easy

Topic:
- String

Approach:
Traverse the string and compare every pair of adjacent
characters.

For each pair:
- Convert both characters to their ASCII values using ord().
- Compute the absolute difference.
- Add it to the total score.

Return the final score.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score