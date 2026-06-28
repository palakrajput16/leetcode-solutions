"""
Problem: 6. Zigzag Conversion

Difficulty: Medium

Topic:
- String
- Simulation

Approach:
Simulate writing the characters row by row in a zigzag pattern.
Maintain a list of strings, one for each row.

Traverse the input string while keeping track of:
- the current row
- the current direction (moving down or up)

Whenever the first or last row is reached, reverse the direction.
Append each character to its corresponding row and finally join
all the rows to obtain the converted string.

Special Case:
If numRows is 1 or greater than or equal to the length of the
string, no zigzag pattern is formed, so return the original string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for char in s:
            rows[currRow] += char

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)