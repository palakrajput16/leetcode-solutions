"""
Problem: 3. Longest Substring Without Repeating Characters

Difficulty: Medium

Topic:
- String
- Sliding Window
- Hash Set

Approach:
Maintain a sliding window using two pointers.
Use a hash set to keep track of characters currently
inside the window. If a duplicate character is found,
shrink the window from the left until the duplicate
is removed. Update the maximum window size after
each expansion.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len