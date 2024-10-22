"""
Title: 344. Reverse String

Difficulty: Easy

Topics: Two Pointers, String

Description: https://leetcode.com/problems/reverse-string/description/

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
APPROACH: Two Pointers 

INTUITION: We want to swap characters with their corresponding character on the opposite end of the list, so we iterate from both ends of the list.

    ALGORITHM: 
        - Iterate i from 0 to len(s)//2 if len(s) is even and iterate i from 0 to len(s)//2 + 1 if len(s) is odd:
            - Swap s[i] with s[len(s) - 1 - i]


COMPLEXITY:
    TIME: O(n), where n is the length of the string
    SPACE: O(1)

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = ((len(s)//2) + 1) if len(s) % 2 == 1 else (len(s)//2)
        for i in range(end):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

    

if __name__=="__main__":
    print(Solution())
