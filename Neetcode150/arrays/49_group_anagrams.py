"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Difficulty: Medium

Problem Description:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Explanation: [explanation]

Example 2:
Input: strs = ["x"]
Output: [["x"]]
Explanation: [explanation]

Example 3:
Input: strs = [""]
Output: [[""]]
Explanation: [explanation]

Constraints:
- 1 <= strs.length <= 1000.
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(m * n)
Space Complexity: O(m)
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_indices = {}

        for i, ana in enumerate(strs):
            key = "".join(sorted(ana))
            if key in ana_indices:
                ana_indices[key].append(ana)
            else:
                ana_indices[key] = [ana]

        return ana_indices.values()


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.groupAnagrams(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.groupAnagrams(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 