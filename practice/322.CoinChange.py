"""
Title: 322. Coin Change 

Difficulty: Medium

Topics: Dynamic Programming, Breadth-First Search, Array

Description: https://leetcode.com/problems/coin-change/

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
APPROACH: Dynamic Programming 

INTUITION: We want to solve smaller versions of our problem in order to solve the big problem, so we want ot find the smallest number of coins needed to 
make smaller amounts, store that information, and use it to find the minimum number of coins needed for our target amount.

    ALGORITHM:
        - If amount is 0 we can just return 0
        - We create an array, memo, of length amount + 1 where memo[i] will store the minimum number of coins needed to get that amount
            - Since we're going to be constantly updating memo[i] with a new minimum we have to initialize all values of memo with an impossibly large value
            - We can also initialize memo[0] to 0 since this is a base case
        - For every index, i, of memo (possible amount less than the target amount):
            - We iterate through all the coin values, c, checking that they are less than or equal to the index (current amount):
                - If so we want to update memo[i] with the minimum between itself and 1 + memo[i - c]
                    - REASONING: 1 (the current coin, c) + memo[i - c] (the minimum number of coins needed to get amount i - c) represents the coin count of a 
                    new combination of coins that yeilds amount. Since we want to always have past memo[i] be as small as possible, we need to check that by 
                    comparing it with the coin count of each new possible coin combination, and updating if a new minimum is found.
        - Once the nested loop is complete we either return memo[amount] or -1 if memo[amount] remains at its initialized value
                

COMPLEXITY:
    - Time: O(amount*coins.length)
    - Space: O(amount)

"""
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # FIRST TRY – Accepted (Beats 39.23% on Runtime)
        memo = [amount+1 for i in range(amount + 1)]

        for i in range(amount + 1):
            if i == 0:
                memo[0] = 0
            else:
                for c in coins:
                    if i - c >= 0:
                        memo[i] = min(memo[i], 1 + memo[i - c])
        
        print(memo)
        return (memo[-1] if memo[-1] < amount + 1 else -1)
    
"""
OPTIMIZATIONS:
    1. Sorting coins at the beginning, and terminating the inner `for c in coins:` loop once i - c is less than 0
    2. Immediately returning 0 if amount equals 0
    3. Making `for c in coins:` the outer loop, and then modifying the inner loop to iterate from the current coin value to amount + 1 
    (i.e. `for i in range(c, amount + 1):`)
        - REASONING: This new inner loop won't even begin if the current coin, c, is greater than the amount
"""

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # SECOND TRY – Optimization 1. added (Beats 45.35% on Runtime)
        memo = [amount+1 for i in range(amount + 1)]
        coins.sort()

        for i in range(amount + 1):
            if i == 0:
                memo[0] = 0
            else:
                for c in coins:
                    if i - c >= 0:
                        memo[i] = min(memo[i], 1 + memo[i - c])
                    else: break
        
        print(memo)
        return (memo[-1] if memo[-1] < amount + 1 else -1)

class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## THIRD TRY – Optimizations 2. and 3. added (Beats 90.39% on Runtime)
        if amount == 0: return 0
        memo = [amount+1 for i in range(amount + 1)]
        memo[0] = 0

        for c in coins:
                for i in range(c, amount + 1): # immediately ends if coin value is greater than amount
                    memo[i] = min(memo[i], 1 + memo[i - c])
        
        # print(memo)
        return (memo[amount] if memo[amount] < amount + 1 else -1)
    
"""
APPROACH: Breadth-First Search (BFS)

INTUITION: 

    ALGORITHM:             

COMPLEXITY:
    TIME: TODO
    SPACE: O(amounts)

"""

class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # FOURTH TRY – Breadth First Search (Beats 99.61% on Runtime)
        if amount == 0: return 0
        
        coin_count = 1 # current coin count
        prev_amounts = set(coins) # amounts that can be made from current and previous coin counts
        amounts = coins # amounts that can be made from the previous coin count

        while amounts:
            if amount in prev_amounts: # checks if amount can be created from the current coin count
                return coin_count
            coin_count += 1
            next_amounts = [] # amounts that can be made from the current coin count
            for c in coins:
                for a in amounts:
                    if not (c + a in prev_amounts) and c + a <= amount:
                        prev_amounts.add(c + a)
                        next_amounts.append(c + a)
            print(next_amounts)
            amounts = next_amounts
        
        return -1 

    

if __name__=="__main__":
    print(Solution1())
