"""
Problem: 1544. Make The String Great

Difficulty: Easy

Topic:
- String
- Stack

Approach:
Use a stack to build the final string.

Traverse each character:
- If the stack is not empty and the current character and the
  top of the stack are the same letter with opposite cases,
  remove the top character.
- Otherwise, push the current character onto the stack.

The ASCII values of uppercase and lowercase versions of the
same letter differ by exactly 32, so we can use this property
to detect removable pairs.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for char in s:

            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)