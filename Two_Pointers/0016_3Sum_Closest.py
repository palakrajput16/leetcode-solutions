"""
Problem: 16. 3Sum Closest

Difficulty: Medium

Topic:
- Array
- Two Pointers
- Sorting

Approach:
Sort the array first.

For each element, fix it as the first number of the triplet.
Use two pointers to search for the remaining two numbers.

For every triplet:
- Compute its sum.
- If it is closer to the target than the previous best sum,
  update the answer.
- If the sum is smaller than the target, move the left pointer
  to increase the sum.
- If the sum is larger than the target, move the right pointer
  to decrease the sum.
- If the sum equals the target, return it immediately because
  it is the closest possible answer.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    left += 1

                elif current > target:
                    right -= 1

                else:
                    return current

        return closest