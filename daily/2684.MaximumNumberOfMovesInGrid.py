"""
Title: 2684. Maximum Number of Moves in a Grid

Difficulty: Medium

Topics: Array, Dynamic Programming (DP), Matrix

Description: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/?envType=daily-question&envId=2024-10-29

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
APPROACH: Bottom-up Dynamic Programming

INTUITION: This is a classic 2D dynamic programming (DP) because the answer to the overall problem can be formulated by building upon the answer to 
smaller subproblems. To find the maximum number of moves we can make starting from the cells in the first column, we find the maximum number of moves it
can take to get to the first column cells from the first column (our base case), and then for each subsequent column in the grid use the previous column
and the given rules of movement to build the solution for a grid that would have ended at that column. We also need store the information from these 
subproblems in an auxilliary grid, and then use that auxilliary grid to answer our overall problems

    ALGORITHM: 
        - Get and store the number of rows (rows) and columns (cols)
        - Initialize a 2D array called dp[][] where all cells in column 0 are 0 and all other cells are -1
            - The 0 value will indicate that the max number of steps to get to the cell is 0 and -1 will indicate that the cell is not reachable from
            the first column based on the given movement rules
        - Intialize an integer called max_moves as 0
        - For all columns from 1 to cols: (NOTE! We want to move column wise since subsequent column cells depend on the cells from the previous column)
            - Assign another name to the current value of the max number of moves (i.e. old_max_moves = max_moves)
            - For all rows from 0 to rows:
                - Initialize an empty array (prevs) to store the max number of moves (dp value) to get all potential previous cells (if they exist)
                - If the value of the grid cell to the upper left of the current grid cell exists, is less than the current grid cell, and is reachable 
                from the first column (the upper left cell's dp value is greater than -1), we append the upper left cell's dp value to prevs
                - If the value of the grid cell to the left of the current grid cell is less than the current grid cell, and is reachable 
                from the first column (the left cell's dp value is greater than -1), we append the left cell's dp value to prevs
                - If the value of the grid cell to the lower left of the current grid cell exists, is less than the current grid cell, and is reachable 
                from the first column (the lower left cell's dp value is greater than -1), we append the lower left cell's dp value to prevs
                - If prevs is still empty or if the maximum value in prevs is -1, then the current cells dp value should remain as -1 to indicate it is
                not reachable
                - If prevs is not empty and has at least one value that is greater than -1, then the dp value at the current cell should be the maximum
                previous dp value in prevs (i.e. the max number of moves to get to previous cells) incremented by 1.
                - We can also update the max_moves variable to be the maximum between the current value of max_moves and the new dp value for the current
                cell
            - Once we have checked and updated all the dp values in the current column accordingly, we should check that the maximum number of moves
            has changed from the value it had at the very start of this column iteration by comparing max_moves to old_max_moves
                - If old_max_moves and max_moves are equal this means that all cells in the current column are unreachable (because every move
                increments the column) and by extension all cells in the columns to follows will also be unreachable
                    - To avoid doing work that we know will not change the max number of moves, we exit the outer loop
                - If old_max_moves and max_moves are not equal, at least one cell in the current column can be reached meaning cells in subsequent columns
                might be able to be reached
                    - In this case we remain in the loop
        - When the outer loop terminates we return the value of max_moves as the solution


COMPLEXITY:
    TIME: O(m*n), where m is the number of rows and n is the number of columns
        - We visit each entry of grid and dp (starting from column 1) one time, and do O(1) time operations at each entry. The number of entries visited
        is given by m*n - m (all entries in the grid minus the number of entries in the column 0)
            - Therefore the overall time complexity is O((m*n - m)*1) which simplifies to O(m*n)
    SPACE: O(m*n), where m is the number of rows and n is the number of columns
        - We have to create an auxilliary array, dp, of the same size as grid, and since grid has m*n entries and all other variables require O(1) space
        the overall space complexity of the solution is O(m*n)

"""
class Solution1: # Beat 53.62% on Runtime
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 if j > 0 else 0 for j in range(cols)] for i in range(rows)]
        max_moves = 0

        for col in range(1, cols):
            _max_moves = max_moves
            for row in range(rows):
                prevs = []
                if row - 1 > -1 and grid[row - 1][col - 1] < grid[row][col]: prevs.append(dp[row - 1][col - 1])
                if grid[row][col - 1] < grid[row][col]: prevs.append(dp[row][col - 1])
                if row + 1 < rows and grid[row + 1][col - 1] < grid[row][col]: prevs.append(dp[row + 1][col - 1])
                if not prevs or max(prevs) == -1: continue
                dp[row][col] = 1 + max(prevs)
                max_moves = max(max_moves, dp[row][col])
            if _max_moves == max_moves: break

        return max_moves
    
"""
OPTIMIZATIONS:
    - Optimizing the operations in the inner loop
        - The prevs array isn't really necessary since if the guards for the previous cells pass we can just update the dp value of the current cell
        to be the maximum between its current value and 1 + the previous cell's dp value.
            - The current cell's dp value should also only be updated if the previous cell's dp value is greater than -1
"""
class Solution2: # Beat 62.32% on Runtime
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 if j > 0 else 0 for j in range(cols)] for i in range(rows)]
        max_moves = 0

        for col in range(1, cols):
            _max_moves = max_moves
            for row in range(rows):
                if row - 1 > -1 and grid[row - 1][col - 1] < grid[row][col] and dp[row - 1][col - 1] != -1: 
                    dp[row][col] = max(dp[row][col], 1 + dp[row - 1][col - 1])
                if grid[row][col - 1] < grid[row][col] and dp[row][col - 1] != -1: 
                    dp[row][col] = max(dp[row][col], 1 + dp[row][col - 1])
                if row + 1 < rows and grid[row + 1][col - 1] < grid[row][col] and dp[row + 1][col - 1] != -1:
                    dp[row][col] = max(dp[row][col], 1 + dp[row + 1][col - 1])
                max_moves = max(max_moves, dp[row][col])
            if _max_moves == max_moves: break

        return max_moves
    
"""
OPTIMIZATIONS:
    - Only maintaining the current and previous column of dp array
        - To update any dp column we only ever need to know the values in the previous dp column so we can make dp only use two columns
        - NOTE! This changes the overall space complexity to O(2*m) which simplifies to O(m)
"""

class Solution3: # Beat 73.91% on Runtime
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 if j > 0 else 0 for j in range(2)] for i in range(rows)] # dp[i][0] is prev and dp[i][1] is curr
        max_moves = 0

        for col in range(1, cols):
            _max_moves = max_moves
            for row in range(rows):
                if row - 1 > -1 and grid[row - 1][col - 1] < grid[row][col] and dp[row - 1][0] != -1: 
                    dp[row][1] = max(dp[row][1], 1 + dp[row - 1][0])
                if grid[row][col - 1] < grid[row][col] and dp[row][0] != -1: 
                    dp[row][1] = max(dp[row][1], 1 + dp[row][0])
                if row + 1 < rows and grid[row + 1][col - 1] < grid[row][col] and dp[row + 1][0] != -1:
                    dp[row][1] = max(dp[row][1], 1 + dp[row + 1][0])
                max_moves = max(max_moves, dp[row][1])
            if _max_moves == max_moves: break
            for row in range(rows):
                dp[row][0] = dp[row][1]
                dp[row][1] = -1

        return max_moves
    
"""
OPTIMIZATIONS:
    - Leveraging the following fact:
        "The maximum number of moves we can make if we start at column 0 is the column index of the maximum reachable column."
        - This is true because every valid move requires that we increment the column by 1, or in other words you cannot reach a cell in column 3 without
        making at least 3 moves AND there is no way you can make more than 3 moves and be in column three
            - This tells us that every reachble cell in a column will have the same dp value and that dp value will be the column's index
                - TLDR: Maintaining integer values representing the maximum number of moves in dp is redundant since we just need to know if the cells
                are reachable or not from the first column.
                    - Instead we can use booleans, True for a reachable cell and False for an unreachable cell
    - Instead of shifting and reassigning values to the two columns of dp, we can just maintain two spearate arrays represent the columns and reassign
    them as needed.
"""

class Solution4: # Beat 98.55% on Runtime
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prev = [True] * rows # all cells in the first column of dp are reachable

        for col in range(1, cols):
            curr = [False] * rows # we initialize cells in the current column as unreachable
            for row in range(rows):
                if row - 1 > -1 and grid[row - 1][col - 1] < grid[row][col]:
                    curr[row] = curr[row] or prev[row - 1] # if prev[row - 1] is reachable then the current cell (curr[row]) is reachable
                if grid[row][col - 1] < grid[row][col]: 
                    curr[row] = curr[row] or prev[row] # if prev[row] is reachable then the current cell (curr[row]) is reachable
                if row + 1 < rows and grid[row + 1][col - 1] < grid[row][col]:
                    curr[row] = curr[row] or prev[row + 1] # if prev[row + 1] is reachable then the current cell (curr[row]) is reachable
            if not sum(curr): return col - 1 # if every cell in the column is unreachable the max number of steps is the number of step to get to the previous column
            prev = curr

        return cols - 1

if __name__=="__main__":
    print(Solution4())
