"""
Problem: 15. 3Sum
Link: https://leetcode.com/problems/3sum/

Difficulty: Medium

Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5


Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_trips = []
        zero_trips_short = []
        nums = sorted(nums)

        if len(nums) < 3 or nums[0] > 0:
            return zero_trips

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):
                if [num_i, num_j] not in zero_trips_short:
                    zero_trips_short.append([num_i, num_j])
                    try:
                        k = nums[i + j + 2:].index(-num_i - num_j)
                        zero_trips.append([num_i, num_j, -num_i - num_j])
                    except:
                        pass

        return zero_trips


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.solution_function(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.solution_function(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 