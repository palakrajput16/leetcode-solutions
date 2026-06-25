"""
Problem: 1929. Concatenation of Array

Difficulty: Easy

Topic:
- Arrays

Approach:
The required array is simply the original array concatenated
with itself. Python's list concatenation operator (+) performs
this directly.

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums