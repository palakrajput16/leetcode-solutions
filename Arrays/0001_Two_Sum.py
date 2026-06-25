"""
Problem: 1. Two Sum

Difficulty: Easy

Topic:
- Arrays
- Hash Map

Approach:
Iterate through the array while storing previously seen numbers
in a hash map. For each element, calculate its complement
(target - current number). If the complement already exists
in the hash map, return the stored index and current index.

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i