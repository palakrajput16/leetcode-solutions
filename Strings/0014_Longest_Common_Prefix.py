"""
Problem: 14. Longest Common Prefix

Difficulty: Easy

Topic:
- String

Approach:
Use the first string as the reference.

Traverse each character of the first string and compare it
with the character at the same position in every other string.

If any string:
- ends before the current position, or
- has a different character,

then the common prefix ends there. Return the substring of the
first string up to that position.

If every character of the first string matches, then the first
string itself is the longest common prefix.

Time Complexity: O(n × m)

where:
n = number of strings
m = length of the shortest common prefix

Space Complexity: O(1)
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        for i in range(len(strs[0])):

            for string in strs[1:]:

                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]