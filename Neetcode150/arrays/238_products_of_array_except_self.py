"""
Problem: 238. Products of Array Except Self
Link: https://leetcode.com/problems/products-of-array-except-self/

Difficulty: Medium

Problem Description:
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
Explanation: [explanation]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
Explanation: [explanation]

Constraints:
- 2 <= nums.length <= 1000
- -20 <= nums[i] <= 20

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in set(nums):
            zero_index_first = nums.index(0)
            if 0 in nums[zero_index_first + 1:]:
                return [0] * len(nums)
            else:
                prod = 1
                for num in nums:
                    if num:
                        prod *= num
                return [0] * zero_index_first + [prod] + [0] * (len(nums) - zero_index_first - 1)
        else:
            response = []
            min_nums = min(nums)
            min_index = nums.index(min_nums)
            max_prod = 1
            for ind, num in enumerate(nums):
                if ind != min_index:
                    max_prod *= num
                
            for ind, num in enumerate(nums):
                if ind == min_index:
                    response.append(max_prod)
                else:
                    response.append(int(max_prod / num * min_nums))

        return response


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.productExceptSelf(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.productExceptSelf(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 