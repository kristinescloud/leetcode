"""
Title: 50. Pow(x, n)

Difficulty: Medium

Topics: Recursion, Math

Description: https://leetcode.com/problems/powx-n/description/

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
Approach: 


Intuition:


Complexity:

"""


class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif x == 1 or n == 0:
            return 1
        else:
            res = 1
            factor = (x if n > 0 else 1/x)
            n = abs(n)

            while n > 0:
                if n % 2 == 1: # when n is odd -> multiply res by factor, decrement n by 1
                    res *= factor
                    n -= 1
                else: # when n is even -> square factor, integer divide n by 2
                    factor *= factor
                    n //= 2
            return res
        
"""
Approach: 


Intuition:


Complexity:

"""
        
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1: return x
        else:
            def get_power(x, n):
                if n == 0: return 1
                else:
                    if n % 2 == 1: return x * get_power(x, n - 1)
                    else:
                        current = get_power(x, n // 2)
                        return current * current
            
            factor = (x if n > 0 else 1/x)
            n = abs(n)
            return get_power(factor, n)

    

if __name__=="__main__":
    print(Solution1().myPow(x = 2.00000, n = 10) == 1024.00000)
    print(Solution1().myPow(x = 2.10000, n = 3) == 9.26100)
    print(Solution1().myPow(x = 2.00000, n = -2) == 0.25000)
    print(Solution1().myPow(x = 0.00001, n = 2147483647) == 0.00000)

    print(Solution2().myPow(x = 2.00000, n = 10) == 1024.00000)
    print(Solution2().myPow(x = 2.10000, n = 3) == 9.26100)
    print(Solution2().myPow(x = 2.00000, n = -2) == 0.25000)
    print(Solution2().myPow(x = 0.00001, n = 2147483647) == 0.00000)



