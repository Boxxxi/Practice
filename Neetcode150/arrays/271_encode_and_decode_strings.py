"""
Problem: 271. Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/

Difficulty: Medium

Problem Description:
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
Explanation: [explanation]

Example 2:
Input: ["neet","code","love","you"]
Output: ["neet","code","love","you"]
Explanation: [explanation]

Constraints:
- 0 <= strs.length < 100
- 0 <= strs[i].length < 200
- strs[i] contains only UTF-8 characters.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(m)
Space Complexity: O(m+n)
- m: sum of lengths of all strings
- n: number of strings
"""


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        if not strs:
            return encoded_str
        for i, _str in enumerate(strs):
            if not _str:
                encoded_str += '##'
            else:
                for j, char in enumerate(_str):
                    if j != len(_str) - 1:
                        encoded_str += f'{ord(char)}#'
                    else:
                        encoded_str += f'{ord(char)}'
            if i != len(strs) - 1:
                encoded_str += '_'

        return encoded_str


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        parts = s.split('_')
        response = []
        for part in parts:
            word = ''
            seps = part.split('#')
            for sep in seps:
                if sep:
                    word += chr(int(sep))
            
            response.append(word)

        return response


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