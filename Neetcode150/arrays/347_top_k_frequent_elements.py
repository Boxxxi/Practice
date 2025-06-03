"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Difficulty: Medium

Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.



Example 1:
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Explanation: [explanation]

Example 2:
Input: nums = [7,7], k = 1

Output: [7]

Explanation: [explanation]

Constraints:
- 1 <= nums.length <= 10^4.
- -1000 <= nums[i] <= 1000
- 1 <= k <= number of distinct elements in nums.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        top_k_freq = set()
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        response = sorted(freq_dict, key=lambda x: freq_dict.get(x), reverse=True)[:k]

        return response


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.topKFrequent(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.topKFrequent(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 