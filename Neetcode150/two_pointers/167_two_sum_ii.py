"""
Problem: 167. Two Sum II
Link: https://leetcode.com/problems/two-sum-ii/

Difficulty: Medium

Problem Description:
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Example 1:
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: [input]
Output: [output]
Explanation: [explanation]

Constraints:
- 2 <= numbers.length <= 1000
- -1000 <= numbers[i] <= 1000
- -1000 <= target <= 1000

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            try:
                j = numbers.index(target - num)
                return [i+1, j+1]
            except:
                continue

        return -1


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