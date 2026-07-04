"""
Problem: 17. Letter Combinations of a Phone Number

Difficulty: Medium

Topic:
- String
- Backtracking

Approach:
Use backtracking to generate every possible letter combination.

Maintain:
- the current index in the digit string
- the current combination being built

For the current digit, try every possible letter mapped to it,
append the letter to the current combination, and recursively
move to the next digit.

When every digit has been processed, add the completed
combination to the answer.

Time Complexity: O(4ⁿ)

where n is the number of digits.
Each digit has at most 4 possible letters.

Space Complexity: O(n)
(Recursion stack, excluding the output list.)
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):

            if index == len(digits):
                result.append(current)
                return

            letters = phone[digits[index]]

            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")

        return result