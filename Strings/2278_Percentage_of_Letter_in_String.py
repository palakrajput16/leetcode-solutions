"""
Problem: 2278. Percentage of Letter in String

Difficulty: Easy

Topic:
- String

Approach:
Traverse the string and count how many times the given letter
appears.

The required percentage is:

(count × 100) // length of string

Integer division automatically rounds the result down.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """

        count = 0

        for char in s:
            if char == letter:
                count += 1

        return (count * 100) // len(s)