"""
Problem: 796. Rotate String

Difficulty: Easy

Topic:
- String

Approach:
A rotated version of a string will always appear as a substring
of the original string concatenated with itself.

For example:

s = "abcde"

s + s = "abcdeabcde"

This contains every possible rotation of "abcde":
abcde, bcdea, cdeab, deabc, and eabcd.

If the lengths of the two strings are different, they can never
be rotations of each other.

Otherwise, return whether goal appears inside s + s.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False

        return goal in (s + s)