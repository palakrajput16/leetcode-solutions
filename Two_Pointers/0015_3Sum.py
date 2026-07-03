"""
Problem: 15. 3Sum

Difficulty: Medium

Topic:
- Array
- Two Pointers
- Sorting

Approach:
Sort the array first.

For each element, treat it as the first number of the triplet.
Then use two pointers to find two remaining numbers whose sum
equals the negative of the current element.

If the total sum is:
- Less than 0, move the left pointer to increase the sum.
- Greater than 0, move the right pointer to decrease the sum.
- Equal to 0, store the triplet and skip duplicate values.

Also skip duplicate first elements to avoid generating the same
triplet multiple times.

Time Complexity: O(n²)
Space Complexity: O(1)
(Excluding the output list.)
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result