"""
Title: 1593. Split a String Into the Max Number of Unique Substrings

Difficulty: Medium

Topics: Backtracking, String, Hash Table

Description: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/?envType=daily-question&envId=2024-10-21

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
APPROACH: Backtracking

INTUITION: TODO #4

    ALGORITHM:


COMPLEXITY: TODO #5
    TIME:
    SPACE:

"""

class Solution1:
    def maxUniqueSplit(self, s: str) -> int:
        return self.backtrack(s, 0, set())
        
    def backtrack(self, s, start, found):
        if start == len(s): return 0

        max_count = 0

        for end in range(start+1, len(s)+1):
            if s[start:end] not in found:
                found.add(s[start:end])
                max_count = max(max_count, 1 + self.backtrack(s, end, found))
                found.remove(s[start:end])
        return max_count

"""
OPTIMIZATIONS:
    TODO #3
"""

class Solution2:
    def maxUniqueSplit(self, s: str) -> int:
        max_count = [0]
        self.backtrack(s, 0, set())
        return max_count[0]
        
    def backtrack(self, s, start, count, max_count, found):
        if count + (len(s) - end) <= max_count[0]: # count + (len(s) - start) == count + 1 + (len(s) - end)
            return
        if start == len(s):
            max_count[0] = max(max_count[0], count)
            return
        for end in range(start+1, len(s)+1):
            if s[start:end] not in found:
                found.add(s[start:end])
                self.backtrack(s, end, count + 1, max_count, found)
                found.remove(s[start:end])
        return

if __name__=="__main__":
    print(Solution1())
