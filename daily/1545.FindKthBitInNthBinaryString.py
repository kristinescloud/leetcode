"""
Title: 1545. Find Kth Bit in Nth Binary String

Difficulty: Medium

Topics: String, Recursion, Simulation

Description: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

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
Approach: Brute Force


Intuition:


Complexity:

"""
class Solution1:
    def findKthBit(self, n: int, k: int) -> str:
        S = "0"

        def invert_then_reverse(s):
            res = ""
            for i in range(len(s) - 1, -1, -1):
                res += ("0" if s[i] == "1" else "1")
            return res

        for i in range(1, n+1):
            prev = S
            S = prev + "1" + invert_then_reverse(prev)

        return S[k - 1]


"""
Approach: Recursion


Intuition:


Complexity:

"""
class Solution2:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return "0"

        length = pow(2,n)

        if k < length // 2: return self.findKthBit(n - 1, k)
        elif k == length // 2: return "1"
        else: return ("1" if self.findKthBit(n - 1, pow(2,n) - k) == "0" else "0")


    

if __name__=="__main__":
    print(Solution1(n=3, k=1) == "0")
    print(Solution1(n=4, k=11) == "1")
    print(Solution1(n=3, k=5) == "0")
    print(Solution1(n=3, k=7) == "1")

    print(Solution2(n=3, k=1) == "0")
    print(Solution2(n=4, k=11) == "1")
    print(Solution2(n=3, k=5) == "0")
    print(Solution2(n=3, k=7) == "1")
