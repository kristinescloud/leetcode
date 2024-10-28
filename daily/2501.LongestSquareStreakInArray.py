"""
Title: 2501. Longest Square Streak in an Array

Difficulty: Medium

Topics: Array, Hash Table, Binary Search, Dynamic Programming, Sorting

Description: https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=daily-question&envId=2024-10-28

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
APPROACH: Binary Search

INTUITION: TODO #7

    ALGORITHM:

COMPLEXITY: TODO #8
    TIME:
    SPACE:

"""
class Solution1: # Beats 50.54% on Runtime
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        max_streak, seen = 0,set()

        for num in nums:
            if num in seen: continue

            curr, streak = num, 1
            while curr * curr <= nums[-1]:
                if self.binary_search(curr * curr, nums):
                    curr *= curr
                    seen.add(curr)
                    streak += 1
                else: break

            if streak > 1: max_streak = max(max_streak, streak)

        return max_streak if max_streak > 1 else -1

    def binary_search(self, target, nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    return True
            return False


"""
APPROACH: Sets

INTUITION: TODO #9

    ALGORITHM:


COMPLEXITY: TODO #10
    TIME:
    SPACE:

"""
class Solution2: # Beats 91.89% on Runtime
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_streak = 0
        max_num = max(nums)
        _nums = set(nums)

        for num in nums:
            streak, curr = 1, num
            while curr in _nums:
                next_num = curr*curr
                if next_num > max_num: break
                elif next_num in _nums:
                    streak += 1
                    curr = next_num
                else: break
            if streak > 1: max_streak = max(max_streak, streak)
        
        return max_streak if max_streak > 1 else -1
    

if __name__=="__main__":
    print(Solution2())
