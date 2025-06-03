"""
Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Difficulty: Easy

Problem Description:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true
Explanation: [explanation]

Example 2:
Input: s = "jar", t = "jam"
Output: false
Explanation: [explanation]

Constraints:
- s and t consist of lowercase English letters.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n + m)
Space Complexity: O(1)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.isAnagram(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.isAnagram(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 