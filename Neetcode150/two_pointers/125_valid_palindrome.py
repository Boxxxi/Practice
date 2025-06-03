"""
Problem: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy

Problem Description:
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: Explanation: "tabacat" is not a palindrome.

Constraints:
- 1 <= s.length <= 1000
- s is made up of only printable ASCII characters.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(1)
"""

import re
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^\w]+|_', '', s)

        str_len = len(s)
        
        return s[:str_len // 2] == s[math.ceil(str_len / 2):][::-1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.isPalindrome(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.isPalindrome(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 