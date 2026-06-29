"""
Problem: 10. Regular Expression Matching

Difficulty: Hard

Topic:
- Dynamic Programming
- String
- Recursion
- Memoization

Approach:
Define dfs(i, j) as whether the substring s[i:] matches the
pattern p[j:].

At every position, first check whether the current characters
match. Two characters match if they are equal or the pattern
contains '.'.

If the next character in the pattern is '*', two choices are
possible:

1. Skip the current character and '*' completely
   (treat '*' as matching zero occurrences).

2. If the current characters match, consume one character from
   the string while keeping the same pattern position because
   '*' can still match more characters.

If there is no '*', simply move to the next character in both
the string and the pattern.

Memoization stores every (i, j) state so that repeated
subproblems are solved only once.

Time Complexity: O(m × n)
Space Complexity: O(m × n)
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}

        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern exhausted
            if j == len(p):
                return i == len(s)

            firstMatch = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                ans = (
                    dfs(i, j + 2) or
                    (firstMatch and dfs(i + 1, j))
                )

            else:

                ans = firstMatch and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)