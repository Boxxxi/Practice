"""
Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Difficulty: Medium

Problem Description:
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true
Explanation: [explanation]

Example 2:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.

Approach:
[Describe your approach to solving the problem]

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

import numpy as np
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rule_sets = {}
        board = np.array(board)
        for i in range(9):
            rule_sets[f"row{i+1}"] = [int(x) for x in board[i, :] if x != "."]
            rule_sets[f"col{i+1}"] = [int(x) for x in board[:, i] if x != "."]
            unit_start_row, unit_start_col = 3 * (i % 3), 3 * (i // 3)
            rule_sets[f"unit{i+1}"] = []
            for j in range(9):
                unit_row, unit_col = unit_start_row + j // 3, unit_start_col + j % 3
                if board[unit_row, unit_col] != ".":
                    rule_sets[f"unit{i+1}"].append(int(board[unit_row, unit_col]))

        for nums in rule_sets.values():
            if len(set(nums)) != len(nums):
                return False

        else:
            return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1_input = None
    expected1 = None
    result1 = solution.isValidSudoku(test1_input)
    print(f"Test 1 passed: {result1 == expected1}")
    
    # Test case 2
    test2_input = None
    expected2 = None
    result2 = solution.isValidSudoku(test2_input)
    print(f"Test 2 passed: {result2 == expected2}") 