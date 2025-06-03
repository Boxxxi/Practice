"""
Problem: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium

Problem Description:
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

![Container With Most Water](../images/11_container_with_most_water.avif)


Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
Explanation: [explanation]

Example 2:
Input: height = [2,2,2]
Output: 4
Explanation: [explanation]

Constraints:
- 2 <= height.length <= 1000
- 0 <= height[i] <= 1000

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_hts = len(heights)
        initial_area = min(heights[0],  heights[-1]) * (len_hts - 1)

        max_area = initial_area

        pointer1 = 0
        pointer2 = len_hts - 1

        while pointer2 > pointer1:
            area = (pointer2 - pointer1) * min(heights[pointer1], heights[pointer2])
            if area > max_area:
                max_area = area
            
            if heights[pointer1] < heights[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1

        return max_area



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