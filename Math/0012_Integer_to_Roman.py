"""
Problem: 12. Integer to Roman

Difficulty: Medium

Topic:
- Math
- String
- Greedy

Approach:
Roman numerals are formed by repeatedly taking the largest
possible Roman value that does not exceed the remaining number.

Store all Roman numeral values (including the special subtractive
cases such as IV, IX, XL, XC, CD, and CM) in descending order.

Traverse the list from largest to smallest. For each value,
append its corresponding Roman symbol while the current number
is greater than or equal to that value, subtracting the value
each time.

Continue until the number becomes zero.

Time Complexity: O(1)
(The number of Roman numeral symbols is fixed.)

Space Complexity: O(1)
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]

        return "".join(result)