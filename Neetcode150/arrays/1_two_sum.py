"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Difficulty: Easy

Problem Description:
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10

Output: [0,2]

Explanation: [explanation]

Example 2:
Input: nums = [5,5], target = 10

Output: [0,1]

Explanation: [explanation]


Constraints:
- 2 <= nums.length <= 1000
- -10,000,000 <= nums[i] <= 10,000,000
- -10,000,000 <= target <= 10,000,000

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in set(nums[i + 1:]):
                return sorted([i, nums[i+1:].index(difference) + i + 1])


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.twoSum(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.twoSum(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 