"""
Problem: 11. Container With Most Water

Difficulty: Medium

Topic:
- Array
- Two Pointers
- Greedy

Approach:
The amount of water stored between two lines is determined by

Area = width × min(leftHeight, rightHeight)

Start with two pointers at the ends of the array, giving the
maximum possible width.

At each step:
1. Compute the current area.
2. Update the maximum area found.
3. Move the pointer pointing to the shorter line inward.

The shorter line limits the height of the container. Moving the
taller line only decreases the width while keeping the limiting
height unchanged, so it cannot produce a larger area.

Continue until the two pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        maxArea = 0

        while left < right:

            width = right - left
            currentArea = width * min(height[left], height[right])

            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea