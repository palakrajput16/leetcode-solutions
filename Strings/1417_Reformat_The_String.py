"""
Problem: 1417. Reformat The String

Difficulty: Easy

Topic:
- String

Approach:
Separate the characters into two lists:
- letters
- digits

If the difference in their counts is greater than 1, it is
impossible to alternate them, so return an empty string.

Otherwise, start with the larger group and alternately append
characters from each list until both are exhausted.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """

        letters = []
        digits = []

        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                digits.append(char)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(digits) > len(letters):
            letters, digits = digits, letters

        result = []

        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])

        if len(letters) > len(digits):
            result.append(letters[-1])

        return "".join(result)