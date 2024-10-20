"""
Title: 1289. Minimum Falling Path Sum II

Difficulty: Hard

Topics: Array; Dynamic Programming; Matrix

Description: https://leetcode.com/problems/minimum-falling-path-sum-ii/description/

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

from math import inf
from typing import *

"""
Approach: 


Intuition:


Complexity:

"""


class Solution1:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for row in range(1, n):
            for col in range(n):
                val = grid[row][col]
                minval = inf
                for i in range(n):
                    if i != col:
                        minval = min(minval, val+grid[row - 1][i])
                grid[row][col] = minval
        
        return min(grid[-1])

"""
Approach: 


Intuition:


Complexity:

"""
class Solution2:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for row in range(1, n):
            minval1, minval2 = inf, inf
            minval1_index = -1

            for i in range(n):
                if grid[row - 1][i] < minval1:
                    minval2 = minval1
                    minval1 = grid[row - 1][i]
                    minval1_index = i
                elif grid[row - 1][i] < minval2:
                    minval2 = grid[row - 1][i]
                
            for col in range(n):
                val = grid[row][col]
                if minval1_index != col:
                    grid[row][col] = val + minval1
                else:
                    grid[row][col] = val + minval2
                
        
        return min(grid[-1])
    

if __name__=="__main__":
    print(Solution1().minFallingPathSum(grid=[[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution1().minFallingPathSum(grid=[[7]]))

    print(Solution2().minFallingPathSum(grid=[[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution2().minFallingPathSum(grid=[[7]]))
