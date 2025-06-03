"""
Problem: 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Difficulty: Medium

Problem Description:
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
Explanation: [explanation]

Constraints:
- 0 <= nums.length <= 1000
- -10^9 <= nums[i] <= 10^9

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = list(sorted(set((nums))))
        if not nums_set:
            return 0

        max_len = 0
        _len = 0
        for i, x in enumerate(nums_set[:-1]):
            if nums_set[i+1] - x == 1:
                _len += 1
            else:
                max_len = max(max_len, _len)
                _len = 0

        if _len:
            max_len = max(max_len, _len)

        return max_len + 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.longestConsecutive(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.longestConsecutive(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 