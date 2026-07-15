"""
Problem: 2451. Odd String Difference

Difficulty: Easy

Topic:
- Array
- String
- Hash Table

Approach:
For each word, compute its difference array where each element
is the difference between two consecutive characters.

Convert the difference array into a tuple so it can be used as
a dictionary key.

Group words having the same difference pattern.

Since exactly one word has a unique difference array, return the
word from the group whose size is one.

Time Complexity: O(n × m)

where:
n = number of words
m = length of each word

Space Complexity: O(n × m)
"""

class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def getDifference(word):

            diff = []

            for i in range(len(word) - 1):
                diff.append(ord(word[i + 1]) - ord(word[i]))

            return tuple(diff)

        groups = {}

        for word in words:

            key = getDifference(word)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        for key in groups:
            if len(groups[key]) == 1:
                return groups[key][0]