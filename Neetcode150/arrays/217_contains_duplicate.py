"""
Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Difficulty: Easy

Problem Description:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true
Explanation: [explanation]

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: [explanation]

Constraints:

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq_vals = set()
        for num in nums:
            if num in unq_vals:
                return True
            else:
                unq_vals.add(num)

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.hasDuplicate(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.hasDuplicate(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 