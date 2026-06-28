"""
Problem: 7. Reverse Integer

Difficulty: Medium

Topic:
- Math

Approach:
Reverse the integer one digit at a time using modulo and integer
division. First, store the sign of the number and work with its
absolute value.

Repeatedly:
- Extract the last digit using modulo (% 10).
- Append it to the reversed number.
- Remove the last digit using integer division (// 10).

After reversing, restore the original sign.

Finally, check whether the reversed integer lies within the
32-bit signed integer range [-2³¹, 2³¹ - 1]. If it overflows,
return 0.

Time Complexity: O(log₁₀(n))
Space Complexity: O(1)
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev