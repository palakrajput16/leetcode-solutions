"""
Problem: 9. Palindrome Number

Difficulty: Easy

Topic:
- Math

Approach:
A negative number can never be a palindrome because of the
leading '-'. Also, any positive number ending in 0 (except 0
itself) cannot be a palindrome.

Reverse only half of the number instead of the entire number.
Keep extracting the last digit from the original number and
append it to the reversed half.

Stop when the reversed half becomes greater than or equal to
the remaining half. At this point:
- For even-length numbers, both halves should be equal.
- For odd-length numbers, ignore the middle digit by dividing
  the reversed half by 10 before comparing.

This avoids reversing the entire integer and prevents overflow.

Time Complexity: O(log₁₀(n))
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedHalf = 0

        while x > reversedHalf:
            reversedHalf = reversedHalf * 10 + x % 10
            x //= 10

        return x == reversedHalf or x == reversedHalf // 10