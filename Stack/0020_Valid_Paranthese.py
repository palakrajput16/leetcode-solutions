"""
Problem: 20. Valid Parentheses

Difficulty: Easy

Topic:
- String
- Stack

Approach:
Use a stack to keep track of opening brackets.

Traverse the string character by character.

- If the current character is an opening bracket, push it onto
  the stack.
- If it is a closing bracket:
    - If the stack is empty, the string is invalid.
    - Otherwise, check whether the top of the stack matches the
      corresponding opening bracket.
    - If it matches, pop the opening bracket.
    - Otherwise, return False.

After processing all characters, the string is valid only if
the stack is empty.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            if char in "([{":
                stack.append(char)

            else:

                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0