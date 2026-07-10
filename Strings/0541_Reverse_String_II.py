"""
Problem: 541. Reverse String II

Difficulty: Easy

Topic:
- String
- Two Pointers

Approach:
Convert the string into a list because Python strings are
immutable.

Process the string in blocks of 2k characters.

For each block:
- Reverse only the first k characters using two pointers.
- Leave the remaining characters unchanged.

Finally, join the character list back into a string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = list(s)

        for start in range(0, len(s), 2 * k):

            left = start
            right = min(start + k - 1, len(s) - 1)

            while left < right:

                s[left], s[right] = s[right], s[left]

                left += 1
                right -= 1

        return "".join(s)