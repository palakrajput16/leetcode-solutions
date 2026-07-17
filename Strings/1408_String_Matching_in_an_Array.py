"""
Problem: 1408. String Matching in an Array

Difficulty: Easy

Topic:
- String

Approach:
For every word, compare it with every other word.

If the current word is a substring of another word (excluding
itself), add it to the answer and stop checking further.

Python's 'in' operator efficiently checks whether one string is
a substring of another.

Time Complexity: O(n² × m)

where:
n = number of words
m = average length of a word

Space Complexity: O(1)
(excluding the output list)
"""

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = []

        for i in range(len(words)):

            for j in range(len(words)):

                if i == j:
                    continue

                if words[i] in words[j]:
                    result.append(words[i])
                    break

        return result