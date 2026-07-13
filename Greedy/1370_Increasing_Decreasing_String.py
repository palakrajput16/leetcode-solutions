"""
Problem: 1370. Increasing Decreasing String

Difficulty: Easy

Topic:
- String
- Greedy

Approach:
Count the frequency of each lowercase letter.

Repeatedly:
1. Traverse from 'a' to 'z'.
   Append each available character once and decrease its count.
2. Traverse from 'z' to 'a'.
   Again append each available character once and decrease its
   count.

Continue until every character has been used.

Time Complexity: O(n)

The alphabet size is fixed (26), so each full pass is constant.

Space Complexity: O(1)
(Uses a fixed-size frequency array.)
"""

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        result = []

        while len(result) < len(s):

            # Increasing
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1

            # Decreasing
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1

        return "".join(result)