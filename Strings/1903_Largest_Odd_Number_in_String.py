"""
Problem: 1903. Largest Odd Number in String

Difficulty: Easy

Topic:
- String

Approach:
A number is odd if its last digit is odd.

Starting from the end of the string, find the first odd digit.
Return the substring from the beginning up to that digit.

If no odd digit exists, return an empty string.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

        for i in range(len(num) - 1, -1, -1):

            if int(num[i]) % 2 == 1:
                return num[:i + 1]

        return ""