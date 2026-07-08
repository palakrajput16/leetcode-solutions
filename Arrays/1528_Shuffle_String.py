"""
Problem: 1528. Shuffle String

Difficulty: Easy

Topic:
- Array
- String

Approach:
Create an empty array of the same length as the input string.

Traverse the string and its corresponding indices together.
For each character, place it directly into its target position
specified by the indices array.

Finally, join the array into a string and return it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        result = [""] * len(s)

        for i in range(len(s)):
            result[indices[i]] = s[i]

        return "".join(result)