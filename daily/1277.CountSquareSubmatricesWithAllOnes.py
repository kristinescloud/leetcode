"""
Title: 1277. Count Square Submatrices with All Ones

Difficulty: Medium

Topics: Array, Dynamic Programming (DP), Matrix

Description: https://leetcode.com/problems/count-square-submatrices-with-all-ones/?envType=daily-question&envId=2024-10-26

"""
from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

"""
APPROACH: Bottom Up Dynamic Programming

INTUITION:
    - We need to find the number of square submatrices containing only ones in a binary matrix. A square submatrix has equal rows and columns, such as 1x1, 2x2, 3x3, and so on.

1x1 submatrices: Each cell with a 1 contributes directly to the count.
Larger submatrices: For submatrices larger than 1x1, the size of the largest square submatrix with its bottom right corner at (i, j) determines the count of possible square submatrices.

Thus, constructing larger submatrices relies on the existence of smaller valid ones.

Tabulation is a dynamic programming technique that involves systematically iterating through all possible combinations of changing parameters. Since tabulation operates iteratively, rather than recursively, it does not require overhead for the recursive stack space, making it more efficient than memoization. We have two variables that change as we progress through the matrix: the current row index and the current column index. To thoroughly explore the combinations, we use two nested loops to iterate through these variables.

First, we establish the base case: if the element at matrix[i][j] is 0, then dp[i][j] = 0, indicating no square submatrix can end at that position.

Our goal is to count the total number of square submatrices filled with all 1s. To achieve this, we traverse the matrix using the outer loop for rows and the inner loop for columns. For each cell containing 1, we calculate the size of the largest square submatrix that can end at that cell by taking the minimum of the square submatrices that can end to the left, above, and diagonally above-left. We update our tabulation matrix with the formula:

    ALGORITHM:


COMPLEXITY:
    TIME: O(n_rows * n_cols), where n_rows is the number of rows in the matrix and n_cols is the number of columns in the matrix.
        - Each cell of matrix is only visited once as we tabulate the running sum of possible all-1, square submatrices achored at each cell
        - Since there are n_rows * n_cols cells, the solution function runs in O(n_rows * n_cols) time
    SPACE: O(1)(!)
        - When using the space already allocated for matrix to create the DP table, the only auxilliary space needed is the storage of key integers so 
        the space complexity is O(1)
        - NOTE(!) If we were not allowed to modify the input matrix then the space complexity would be O(n_rows * n_cols) since there is a DP value to
        be stored at each cell

"""
class Solution1:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        square_count = 0
        # populate memo with base cases:
        memo = [[-1 if j != cols - 1 and i != rows - 1 else matrix[i][j] for j in range(cols)] for i in range(rows)]

        # iteratively populate the rest of memo
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 or j == cols - 1:
                    square_count += memo[i][j]
                elif matrix[i][j]:
                    memo[i][j] = 1 + min(memo[i][j + 1], min(memo[i + 1][j], memo[i + 1][j + 1]))
                    square_count += memo[i][j]
                else: memo[i][j] = 0
        
        return(square_count)
    
"""
OPTIMIZATIONS
    1. Using the input matrix to calculate and store the corresponding DP table values
    2. Play with the order of conditional statements to try to improve runtime
"""

class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        square_count = 0

        for i in range(rows - 2, -1, -1):
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] and j != cols - 1:
                    matrix[i][j] = 1 + min(matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1])
                square_count += matrix[i][j]
        
        return square_count + sum(matrix[-1])

if __name__=="__main__":
    print(Solution2())
