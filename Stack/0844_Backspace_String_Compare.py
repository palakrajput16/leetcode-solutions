"""
Problem: 844. Backspace String Compare

Difficulty: Easy

Topic:
- String
- Stack

Approach:
Simulate typing into a text editor using a stack.

For each character:
- If it is a letter, push it onto the stack.
- If it is '#', remove the most recently added character
  (if the stack is not empty).

Process both strings independently and compare the final
contents of the stacks.

Time Complexity: O(n + m)

where:
n = length of s
m = length of t

Space Complexity: O(n + m)
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def build(string):

            stack = []

            for char in string:

                if char != "#":
                    stack.append(char)

                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)