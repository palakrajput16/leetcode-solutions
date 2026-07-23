"""
Problem: 345. Reverse Vowels of a String

Difficulty: Easy

Topic:
- String
- Two Pointers

Approach:
Use two pointers:
- One starts from the beginning.
- One starts from the end.

Move each pointer until it reaches a vowel.
When both point to vowels, swap them.

Continue until the pointers meet.

A set is used for fast vowel lookup.

Time Complexity: O(n)
Space Complexity: O(n)

(The string is converted into a list since Python strings are
immutable.)
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set("aeiouAEIOU")

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)