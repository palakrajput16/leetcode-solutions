"""
Problem: 8. String to Integer (atoi)

Difficulty: Medium

Topic:
- String
- Simulation

Approach:
Parse the string from left to right according to the given rules.

Steps:
1. Skip all leading whitespace.
2. Check for an optional '+' or '-' sign.
3. Read consecutive digits and construct the integer.
4. Stop reading when a non-digit character is encountered.
5. Apply the sign to the number.
6. Clamp the result within the 32-bit signed integer range
   [-2³¹, 2³¹ - 1].

If no digits are found after processing whitespace and the
optional sign, return 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Determine sign
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # Build the number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num