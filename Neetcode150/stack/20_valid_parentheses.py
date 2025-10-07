"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy

Problem Description:
You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return `true` if `s` is a valid string, and `false` otherwise.

Example 1:
Input: s = "[]"
Output: true
Explanation: [explanation]

Example 2:
Input: s = "[]"
Output: true
Explanation: [explanation]

Constraints:
- 1 <= s.length <= 1000

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        last_open = s[0]

        for char in s[1:]:
            if char == '(':
                last_open += '('
            elif char == '{':
                last_open += '{'
            elif char == '[':
                last_open += '['
            elif char == ')' and last_open and last_open[-1] == '(':
                last_open = last_open[:-1]
            elif char == '}' and last_open and last_open[-1] == '{':
                last_open = last_open[:-1]
            elif char == ']' and last_open and last_open[-1] == '[':
                last_open = last_open[:-1]
            else:
                return False

        if last_open:
            return False

        return True


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