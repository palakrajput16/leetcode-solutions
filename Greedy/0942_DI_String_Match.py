"""
Problem: 942. DI String Match

Difficulty: Easy

Topic:
- Array
- Greedy

Approach:
Maintain two pointers representing the smallest and largest
unused numbers.

Initially:
- low = 0
- high = n

Traverse the string:
- If the current character is 'I', append the smallest available
  number and increment low.
- If it is 'D', append the largest available number gitand decrement
  high.

After processing every character, one number remains.
Append it to complete the permutation.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        low = 0
        high = len(s)

        result = []

        for char in s:

            if char == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        result.append(low)

        return result