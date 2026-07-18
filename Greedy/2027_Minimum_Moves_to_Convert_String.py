"""
Problem: 2027. Minimum Moves to Convert String

Difficulty: Easy

Topic:
- String
- Greedy

Approach:
Traverse the string from left to right.

- If the current character is 'O', simply move to the next position.
- If the current character is 'X', perform one move.
  This converts the current character and the next two characters
  to 'O', so skip all three positions.

Repeat until the entire string is processed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """

        moves = 0
        i = 0

        while i < len(s):

            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1

        return moves