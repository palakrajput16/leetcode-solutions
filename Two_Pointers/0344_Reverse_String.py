"""
Problem: 344. Reverse String

Difficulty: Easy

Topic:
- String
- Two Pointers

Approach:
Use two pointers, one starting from the beginning of the array
and the other from the end.

While the two pointers have not crossed:
- Swap the characters at the two pointers.
- Move the left pointer one step to the right.
- Move the right pointer one step to the left.

Since characters are swapped directly in the input array, the
string is reversed in-place without using extra memory.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1